from django.shortcuts import render, redirect


from .forms import SignUpForm, UserProfileForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            return redirect('login')
    else:
        form = SignUpForm()
        profile_form = UserProfileForm()
    return render(request, 'registration/signup.html', {'form': form, 'profile_form': profile_form})
