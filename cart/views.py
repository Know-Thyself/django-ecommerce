from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def cart_summary(request):
    return render(request, 'cart-summary.html')


def add_to_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productId'))
        product_quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add_to_cart(product, product_quantity)
        response = JsonResponse(
            {'product_name': product.title, 'product_quantity': product_quantity}
        )
        return response


def update_cart(request):
    pass


def remove_from_cart(request):
    pass
