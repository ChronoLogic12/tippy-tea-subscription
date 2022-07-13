from django.shortcuts import render, get_object_or_404

from .models import Subscription


def subscriptions(request):
    """ Display subscription options """

    if request.method == 'GET':
        template = 'subscriptions/subscriptions.html'
        classic = get_object_or_404(Subscription, name="classic")
        large = get_object_or_404(Subscription, name="large")
        discovery = get_object_or_404(Subscription, name="discovery")
        
        context = {
            'classic': classic,
            'large': large,
            'discovery': discovery,
        }

        return render(request, template, context, status=200)