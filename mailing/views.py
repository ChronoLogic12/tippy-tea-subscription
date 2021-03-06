from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.views.defaults import server_error


from .models import Mailing
from profiles.models import Profile
from .forms import MailingForm, MassEmailForm


def mailing(request):
    """ Display form to subscribe to mailing list """
    try:
        if request.method == 'POST':
            form = MailingForm(request.POST)
            if form.is_valid():
                if not Mailing.objects.filter(email=form.cleaned_data['email']).exists():
                    form.save()
                    messages.success(request, 'Thank you for subscribing to our mailing list')
                    if Profile.objects.filter(email=form.cleaned_data['email']).exists():
                        Profile.objects.filter(email=form.cleaned_data['email']).update(mailing=True)
                    return(redirect(reverse('home')))
                else:
                    messages.info(request, "This email is already registered.")
            else:
                messages.error(request, "Signup failed. Please ensure the form is valid.")
        else:
            if request.user.is_authenticated:
                form = MailingForm(instance=request.user.profile)
            else:
                form = MailingForm()

        template = 'mailing/mailing.html'
        
        context = {
            'form': form,
        }

        return render(request, template, context)
    except Exception:
        return server_error(request)


@login_required
def send_newsletter(request):
    """ Send newsletter to all email addresses on mailing list """
    try:
        if not request.user.is_superuser:
            messages.error(request, "Sorry, only accessible by site owners.")
            return redirect(reverse("home"))
        if request.method == 'POST':
            form = MassEmailForm(request.POST)
            if form.is_valid():
                for email in Mailing.objects.values_list('email'):
                    send_mail(
                        form.cleaned_data['subject'],
                        form.cleaned_data['message'],
                        settings.EMAIL_HOST_USER,
                        email,
                        fail_silently=False,
                    )
                messages.success(request, 'Newsletter successfully sent')
                return(redirect(reverse('send_newsletter')))
            else:
                messages.info(request, "Failed to send newsletter. Please ensure the form is valid.")
        else:
            form = MassEmailForm()

        template = 'mailing/send_newsletter.html'
        
        context = {
            'form': form,
        }

        return render(request, template, context)
    except Exception:
        return server_error(request)


def newsletter_unsubscribe(request):
    """ Remove an email address from the site mailing lits """
    try:
        if request.method == 'POST':
            form = MailingForm(request.POST or None)
            if form.is_valid():
                if Mailing.objects.filter(email=form.cleaned_data['email']).exists():
                    Mailing.objects.filter(email=form.cleaned_data['email']).delete()
                    messages.success(request, 'Email successfully removed from mailing list.')
                    if Profile.objects.filter(email=form.cleaned_data['email']).exists():
                        Profile.objects.filter(email=form.cleaned_data['email']).update(mailing=False)
                    return(redirect(reverse('home')))
                else:
                    messages.info(request, "This email is not currently registered.")
            else:
                messages.error(request, "Newsletter unsubscribe failed. Please ensure the form is valid.")
        else:
            if request.user.is_authenticated:
                form = MailingForm(instance=request.user.profile)
            else:
                form = MailingForm()

        template = 'mailing/newsletter_unsubscribe.html'
        
        context = {
            'form': form,
        }

        return render(request, template, context)
    except Exception:
        return server_error(request)