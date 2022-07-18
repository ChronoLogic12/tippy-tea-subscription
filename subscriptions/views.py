from ast import Subscript
from django.shortcuts import render, get_object_or_404

from djstripe.models import Plan
import stripe

from subscriptions.forms import SubscriptionForm


def subscriptions(request):
    """ Display subscription options """

    if request.method == 'GET':
        template = 'subscriptions/subscriptions.html'
        plans = Plan.objects.all().order_by("amount")
        context = {
            'plans': plans,
        }

        return render(request, template, context, status=200)

# def edit_subscription(request, subscription_id):
#     """ Edit subscription details in stripe """
#     if request.method == 'POST':
#         form = SubscriptionForm(request.POST, instance=subscription_id)
#         # if form.is_valid():


#     product = Product.objects.all()
#     template = 'subscriptions/edit_subscription.html'
#     return render(request, template, context, status=200)