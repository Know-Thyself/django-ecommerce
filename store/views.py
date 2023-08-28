from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def category(_):
    categories = Category.objects.all()
    return {'categories': categories}


def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'store/product-info.html', context)

