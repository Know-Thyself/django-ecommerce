from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from .forms import UserRegistrationForm, LoginForm, UpdateUserForm
from payment.forms import ShippingForm
from payment.models import ShippingAddressModel
from .token import user_tokenizer_generate
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from os import environ
from dotenv import load_dotenv

load_dotenv()


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
                'verification/email/email-verification.html',
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
    return render(request, 'verification/email/email-verification-sent.html')


def email_verification_failed(request):
    return render(request, 'verification/email/email-verification-failed.html')


def email_verification_success(request):
    return render(request, 'verification/email/email-verification-success.html')


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                request.session['username'] = username
                messages.success(
                    request, f'Welcome {username}! You have successfully logged in!'
                )
                return redirect('dashboard')
    context = {'form': form}
    return render(request, 'account/user-login.html', context)


@login_required(login_url='user-login')
def dashboard(request):
    username = request.session.get('username')
    context = {'username': username}
    return render(request, 'account/dashboard.html', context)


@login_required(login_url='user-login')
def user_logout(request):
    # logout(request)
    try:
        for key in list(request.session.keys()):
            if key == environ.get('CART_SESSION_KEY'):
                continue
            else:
                del request.session[key]
    except KeyError:
        pass
    return redirect('store')


@login_required(login_url='user-login')
def manage_profile(request):
    user = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        user = UpdateUserForm(request.POST, instance=request.user)
        if user.is_valid():
            user.save()
            messages.success(request, 'Your account is successfully updated!')
            return redirect('dashboard')

    context = {'user': user}

    return render(request, 'account/manage-profile.html', context)


@login_required(login_url='user-login')
def delete_account(request):
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Your account is successfully removed!')
        return redirect('store')

    return render(request, 'account/delete-account.html')


@login_required(login_url='user-login')
def shipping(request):
    try:
        shipping = ShippingAddressModel.objects.get(user=request.user.id)
    except ShippingAddressModel.DoesNotExist:
        shipping = None

    form = ShippingForm(instance=shipping)

    if request.method == 'POST':
        form = ShippingForm(request.POST, instance=shipping)
        if form.is_valid():
            # Assign the user fk on the object
            shipping_address = form.save(commit=False)
            # Adding the fk
            shipping_address.user = request.user
            shipping_address.save()

            return redirect('dashboard')
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        print(user.email)
        context = {'form': form, 'user': user}
        return render(request, 'account/shipping.html', context=context)
