# This code is heavily adapted from the stripe billing quickstart code found here (https://stripe.com/docs/billing/quickstart)

from dataclasses import field
from itertools import product
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decouple import config
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.views.defaults import page_not_found, server_error
from django.http import JsonResponse
from django.core.mail import send_mail

from profiles.forms import ProfileForm
from profiles.models import Profile
from mailing.models import Mailing
from checkout.models import Order
from django.contrib.auth.models import User
from stripe import Subscription, Customer

from djstripe.models import Plan, Product

import stripe
from django.conf import settings


# Test secret API key.
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


@login_required
@require_POST
def checkout(request):
    try:
      plan = Plan.objects.get(id=request.POST['plan_id'])
    except Exception as e:
      return page_not_found(request, exception=e)
    template = 'checkout/checkout.html'
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile, fields_required=True)
    context = {
        'form': form,
        'plan': plan,
        'PRICE_LOOKUP_KEY': request.POST['plan_id'],
    }

    return render(request, template, context)


@require_POST
@csrf_exempt
def create_checkout_session(request):
    try:
        profile = get_object_or_404(Profile, user=request.user)
        form = ProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
            if form.cleaned_data['mailing']:
                if not Mailing.objects.all().filter(email=profile.email).exists():
                    Mailing.objects.create(email=form.cleaned_data['email'])
                else:
                    Mailing.objects.filter(email=profile.email).update(email=form.cleaned_data['email'])
            else:
                if Mailing.objects.all().filter(email=profile.email).exists():
                    Mailing.objects.all().filter(email=profile.email).delete()
            form.save()
        else:
            messages.error(request, "Update failed. Please ensure your delivery information is valid.")
            return redirect(reverse('subscriptions'))

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': request.POST['lookup_key'],
                    'quantity': 1,
                },
            ],
            customer=profile.customer_id,
            mode='subscription',
            success_url= f'http{"s" if "tippy" in request.get_host() else ""}://{request.get_host()}/checkout/success/' + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url= f'http{"s" if "tippy" in request.get_host() else ""}://{request.get_host()}/checkout/cancel/'
        )
        return redirect(checkout_session.url)
    except Exception as e:
        print(e)
        return server_error(request)

@login_required
@require_POST
@csrf_exempt
def customer_portal(request):
    profile = get_object_or_404(Profile, user=request.user)
    if not profile.customer_id:
        messages.error(request, 'Error creating portal, no active subscriptions.')
        
    portalSession = stripe.billing_portal.Session.create(
        customer = profile.customer_id,
        return_url = f'http{"s" if "tippy" in request.get_host() else ""}://{request.get_host()}/profile/'
    )
    return redirect(portalSession.url, code=303)

@require_POST
@csrf_exempt
def webhook_received(request):
	try:
		webhook_secret = settings.DJSTRIPE_WEBHOOK_SECRET
		request_data = request.POST
		if webhook_secret:
			signature = request.META['HTTP_STRIPE_SIGNATURE']
			event = stripe.Webhook.construct_event(
			payload=request.body, sig_header=signature, secret=webhook_secret)
			data = event['data']
			event_type = event['type']
		else:
			data = request_data['data']
			event_type = request_data['type']
		data_object = data['object']
		if event_type == 'customer.subscription.created':
			subscription = Subscription.retrieve(data_object.id)
			customer = Customer.retrieve(subscription.customer)
			user = User.objects.get(email=customer.email)
			product = Product.objects.get(id=subscription.plan.product)
			order = Order(user=user, product=product)
			order.save()
			send_mail('Tippy - Order confirmation', 
			f'Your order of {product.name} has been placed. Order number: {order.order_number}',
			settings.EMAIL_HOST_USER,
			[customer.email],
			fail_silently=False,
			)
		elif event_type == 'customer.subscription.deleted':
			subscription = Subscription.retrieve("sub_1LN132GB1o2PoEdcMFGvTTLs")
			customer = Customer.retrieve(subscription.customer)
			user = User.objects.get(email=customer.email)
			product = Product.objects.get(id=subscription.plan.product)
			order = Order.objects.filter(user=user, product=product).first()
			order.delete()
		return JsonResponse({'status': 'success'})
	except Exception as e:
		return JsonResponse({'error': e})


@login_required
def success(request):
	try:
		session_id = request.GET.get('session_id', '')
		if session_id == '':
			return redirect(reverse('home'))
		profile = get_object_or_404(Profile, user=request.user)
		session = stripe.checkout.Session.retrieve(id=session_id, expand=['subscription.plan.product'])
		if not profile.customer_id:
			customer = session.customer
			profile.customer_id = customer
			profile.save()
		product = session.subscription.plan.product 
		template = 'checkout/success.html'
		context = {
		'product': product,
		}
		return render(request, template, context)
	except Exception as e:
		print(e)
		return server_error(request)

def cancel(request):
  return render(request, 'checkout/cancel.html',)

