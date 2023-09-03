from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from .forms import UserRegistrationForm, LoginForm
from .token import user_tokenizer_generate
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth


def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            # Email verification
            current_site = get_current_site(request)
            subject = 'Account Verification Email'
            message = render_to_string(
                'verification/email-verification.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': user_tokenizer_generate.make_token(user),
                },
            )
            user.email_user(subject, message)
            return redirect('email-verification-sent')

    return render(request, 'registration/register.html', {'form': form})


def email_verification(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)

    if user and user_tokenizer_generate.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('email-verification-success')

    return redirect('email-verification-failed')


def email_verification_sent(request):
    return render(request, 'verification/email-verification-sent.html')


def email_verification_failed(request):
    return render(request, 'verification/email-verification-failed.html')


def email_verification_success(request):
    return render(request, 'verification/email-verification-success.html')


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        print(form.is_valid(), 'is_valid')
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user, '<-----user')
            if user is not None:
                auth.login(request=request, user=user)
                return redirect('dashboard')
    context = {'form': form}
    return render(request, 'account/user-login.html', context)


def dashboard(request):
    return render(request, 'account/dashboard.html' )
