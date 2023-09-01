from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('') # TODO - redirect to login page when created

    return render(request, 'register.html', {'form': form})
