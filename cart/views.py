from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart-summary.html', {'cart': cart})


def add_to_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productId'))
        product_quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add_to_cart(product=product, quantity=product_quantity)
        cart_quantity = cart.get_cart_quantity()
        response = JsonResponse({'quantity': cart_quantity})
        return response


def remove_from_cart(request):
    cart = Cart(request)
    if request.GET.get('action') == 'delete':
        product_id = int(request.GET.get('productId'))
        cart.remove_from_cart(product=product_id)
        cart_quantity = cart.get_cart_quantity()
        cart_total = cart.get_total_price()
        response = JsonResponse({'quantity': cart_quantity, 'total': cart_total})
        return response


def update_cart(request):
    cart = Cart(request)
    if request.GET.get('action') == 'put':
        product_id = int(request.GET.get('productId'))
        cart_quantity = int(request.GET.get('quantity'))
        cart.update_cart(id=product_id, quantity=cart_quantity)
        cart_quantity = cart.get_cart_quantity()
        cart_total = cart.get_total_price()
        sub_total = cart.get_sub_total(id=product_id)
        response = JsonResponse(
            {'quantity': cart_quantity, 'sub_total': sub_total, 'total': cart_total}
        )
        return response
