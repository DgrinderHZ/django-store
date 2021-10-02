from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

from .utils import send_confirmation_email
from .forms import SignUpForm, EditProfileForm
from .tokens import confirm_email_token_generator
from .models import User


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # TODO dont save 2 times (different mail is a must)
            user.is_active = False
            user.save()

            send_confirmation_email(request, user)

            return render(request, 'registration/signup_success.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html',
                  {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_detail')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {
        'form': form
    })


def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    if confirm_email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponseBadRequest('Bad Token')


@login_required
def user_detail(request):
    return render(request, 'registration/user_detail.html')
