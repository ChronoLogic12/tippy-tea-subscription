from django.shortcuts import render

from djstripe.models import Plan

def subscriptions(request):
    """ Display subscription options """

    if request.method == 'GET':
        template = 'subscriptions/subscriptions.html'
        plans = Plan.objects.all().order_by("amount")
        context = {
            'plans': plans,
        }

        return render(request, template, context, status=200)
