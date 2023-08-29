from django.urls import path
from . import views

urlpatterns = [
    # Cart Summary
    path('', views.cart_summary, name='cart-summary'),
    path('add/', views.add_to_cart, name='add-to-cart'),
    path('remove/', views.remove_from_cart, name='remove-from-cart'),
    path('update/', views.update_cart, name='update-cart'),

]