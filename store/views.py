from django.shortcuts import render
from .models import Category, Product

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def category(_):
    categories = Category.objects.all()
    return {'categories': categories}

