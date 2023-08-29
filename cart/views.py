from django.shortcuts import render


def cart_summary(request):
    return render(request, 'cart-summary.html')


def add_to_cart(request):
    pass


def update_cart(request):
    pass


def remove_from_cart(request):
    pass
