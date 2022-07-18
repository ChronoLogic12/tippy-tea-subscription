# This code is heavily adapted from the stripe billing quickstart code found here (https://stripe.com/docs/billing/quickstart)

from dataclasses import field
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decouple import config
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.views.defaults import page_not_found, server_error
from django.http import JsonResponse

from profiles.forms import ProfileForm
from profiles.models import Profile
from mailing.models import Mailing

from djstripe.models import Plan

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
def webhook_received(request):
    # Replace this endpoint secret with your endpoint's unique secret
    # If you are testing with the CLI, find the secret by running 'stripe listen'
    # If you are using an endpoint defined with the API or dashboard, look in your webhook settings
    # at https://dashboard.stripe.com/webhooks
    webhook_secret = settings.STRIPE_WH_SECRET
    request_data = request.POST

    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']

    print('event ' + event_type)

    if event_type == 'checkout.session.completed':
        messages.success(request, 'Payment succeeded!')
    elif event_type == 'customer.subscription.trial_will_end':
        print('Subscription trial will end')
    elif event_type == 'customer.subscription.created':
        print('Subscription created %s', event.id)
    elif event_type == 'customer.subscription.updated':
        print('Subscription created %s', event.id)
    elif event_type == 'customer.subscription.deleted':
        # handle subscription canceled automatically based
        # upon your subscription settings. Or if the user cancels it.
        print('Subscription canceled: %s', event.id)

    return JsonResponse({'status': 'success'})


@login_required
def success(request):
    session_id = request.GET.get('session_id', '')
    if session_id == '':
        return redirect(reverse('home'))
    profile = get_object_or_404(Profile, user=request.user)
    if not profile.customer_id:
        session = stripe.checkout.Session.retrieve(session_id)
        customer = session.customer
        profile.customer_id = customer
        profile.save()
    return render(request, 'checkout/success.html')

def cancel(request):
  return render(request, 'checkout/cancel.html')
