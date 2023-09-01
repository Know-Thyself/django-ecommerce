from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')  # TODO - redirect to login page when created

    return render(request, 'registration/register.html', {'form': form})


def email_verification(request):
    pass


def email_verification_failed(request):
    pass


def email_verification_success(request):
    pass


def email_verification_sent(request):
    pass
