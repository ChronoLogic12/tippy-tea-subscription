from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile
from mailing.models import Mailing
from .forms import ProfileForm

@login_required
def profile(request):
    """ Display the user's profile """
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            if form.cleaned_data['mailing']:
                if not Mailing.objects.all().filter(email=profile.email).exists():
                    Mailing.objects.create(email=form.cleaned_data['email'])
                    messages.success(request, 'Email successfully added to newsletter')
                else:
                    Mailing.objects.filter(email=profile.email).update(email=form.cleaned_data['email'])
            else:
                if Mailing.objects.all().filter(email=profile.email).exists():
                    Mailing.objects.all().filter(email=profile.email).delete()
                    messages.info(request, 'Email successfully removed from mailing list')
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, "Update failed. Please ensure the form is valid.")
    else:
        form = ProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'on_profile_page': True,
    }

    return render(request, template, context)

@login_required
def delete_profile(request):
    """ Delete User profile """
    if request.method == 'DELETE':
        user=request.user
        user.delete()
        messages.success(request, 'User profile deleted!')
        return redirect(reverse('home'))
