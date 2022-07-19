from django.shortcuts import render
from django.views.defaults import server_error

from djstripe.models import Plan

def subscriptions(request):
    """ Display subscription options """
    try:
        if request.method == 'GET':
            template = 'subscriptions/subscriptions.html'
            plans = Plan.objects.all().order_by("amount")
            context = {
                'plans': plans,
            }

            return render(request, template, context, status=200)
    except Exception:
        return server_error(request)
