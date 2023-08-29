from django.urls import path
from . import views

urlpatterns = [
    # Storefront
    path('', views.store, name='store'),
    # Individual product
    path('product/<slug:product_slug>', views.get_product_info, name='product-info'),
    # Individual category
    path(
        'search/<slug:category_slug>',
        views.get_products_by_category,
        name='category',
    ),
]
