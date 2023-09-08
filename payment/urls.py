from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete-order/', views.complete_order, name='complete-order'),
    path('success/', views.payment_success, name='payment-success'),
    path('failed/', views.payment_failed, name='payment-failed'),
]
