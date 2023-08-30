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


def update_cart(request):
    pass


def remove_from_cart(request):
    pass
