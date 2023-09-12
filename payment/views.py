from django.shortcuts import render, redirect
from .models import ShippingAddress, Order, OrderedItem
from django.http import JsonResponse
from .forms import ShippingForm
from cart.cart import Cart
from dotenv import load_dotenv
from os import environ

load_dotenv()


def payment_success(request):
    return render(request, 'payment-success.html')


def process_payment(request):
    # clear shopping cart
    # for key in list(request.session.keys()):
    #     if key == environ.get('CART_SESSION_KEY'):
    #         del request.session[key]
    context = {'customer_name': 'customer_name'}
    return render(request, 'process-payment.html', context=context)


def payment_failed(request):
    return render(request, 'payment-failed.html')


def checkout(request):
    order_detail = {}
    try:
        # If the user is authenticated and registered their shipping address previously
        shipping_address = ShippingAddress.objects.get(user=request.user.id)
    except ShippingAddress.DoesNotExist:
        # If the user is a guest or authenticated but did not register their shipping address
        shipping_address = None
    except ShippingAddress.MultipleObjectsReturned:
        shipping_address = ShippingAddress.objects.filter(user=request.user.id).last()
        outdated_addresses = ShippingAddress.objects.filter(
            user=request.user.id
        ).exclude(id=shipping_address.id)
        outdated_addresses.delete()
    # The form will either be prefilled or empty depending on the above conditions
    form = ShippingForm(instance=shipping_address)

    if request.method == 'POST':
        print('yessssssssss')
        # data = {
        #     'full_name': request.POST.get('name'),
        #     'email': request.POST.get('email'),
        #     'address1': request.POST.get('address1'),
        #     'address2': request.POST.get('address2'),
        #     'city': request.POST.get('city'),
        #     'state': request.POST.get('state'),
        #     'zipcode': request.POST.get('zipcode'),
        # }
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        print(full_name, email, address1, address2, city)
        # form = ShippingForm(request.POST, instance=shipping_address)
        form = ShippingForm(request.POST, instance=shipping_address)
        if form.is_valid():
            shipping = form.save()
            # Adding the fk
            shipping.user = request.user
            shipping.save()
            for key, val in request.POST.items():
                if key != 'csrfmiddlewaretoken':
                    order_detail[key] = val
            cart = Cart(request)
            total_price = cart.get_total_price()
            order_detail['amount_paid'] = total_price
            if request.user.is_authenticated:
                print(request.user)
                order_detail['user'] = request.user
                order = Order.objects.create(**order_detail)
                order_id = order.pk
                for item in cart:
                    OrderedItem.objects.create(
                        order_id=order_id,
                        product=item['product'],
                        quantity=item['quantity'],
                        unit_price=item['price'],
                        user=request.user,
                    )
            else:
                order = Order.objects.create(**order_detail)
                order_id = order.pk
                for item in cart:
                    OrderedItem.objects.create(
                        order_id=order_id,
                        product=item['product'],
                        quantity=item['quantity'],
                        unit_price=item['price'],
                    )
            print(request.session)
            return redirect('process-payment')
            # response = JsonResponse({'msg': 'Success!'})
            # return response
        else:
            return redirect('payment-failed')

    context = {'form': form}
    return render(request, 'shipping-address.html', context=context)


def complete_order(request):
    if request.method == 'POST':
        print(request.GET.get('data'))
        pass


def export_env(_):
    return {'SANDBOX_CLIENT_ID': environ.get('SANDBOX_CLIENT_ID')}

def customer_context(name):
    return {'customer_name': name}
