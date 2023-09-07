from django.shortcuts import render, redirect
from .models import ShippingAddressModel
from .forms import ShippingForm


def payment(request):
    return render(request, 'payment.html')


def payment_success(request):
    return render(request, 'payment-success.html')


def payment_failed(request):
    return render(request, 'payment-failed.html')



def checkout(request):
    try:
        shipping_address = ShippingAddressModel.objects.get(user=request.user.id)
    except ShippingAddressModel.DoesNotExist:
        shipping_address = None

    form = ShippingForm(instance=shipping_address)

    if request.method == 'POST':
        form = ShippingForm(request.POST, instance=shipping_address)
        if form.is_valid():
            shipping_address = form.save(commit=False)
            shipping_address.save()

            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'checkout.html', context=context)
