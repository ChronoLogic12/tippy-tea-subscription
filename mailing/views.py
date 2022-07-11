from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Mailing
from .forms import MailingForm
from django.contrib import messages


def mailing(request):
    """ Display form to subscribe to mailing list """
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            if not Mailing.objects.filter(email=form.cleaned_data['email']).exists():
                form.save()
                messages.success(request, 'Thank you for subscribing to our mailing list')
            else:
                messages.info(request, "This email is already registered.")
        else:
            messages.error(request, "Signup failed. Please ensure the form is valid.")
    else:
        if request.user.is_authenticated:
            form = MailingForm(instance=request.user)
        else:
            form = MailingForm()

    template = 'mailing/mailing.html'
    
    context = {
        'form': form,
    }

    return render(request, template, context)
