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


def get_product_info(request, product_slug):
    product = get_object_or_404(
        Product, slug=product_slug
    )  # Quering the Product database table where slug is equal to the  product slug
    context = {'product': product}
    return render(request, 'store/product-info.html', context)


def get_products_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {'category': category, 'products': products}
    return render(request, 'store/products-by-category.html', context)
