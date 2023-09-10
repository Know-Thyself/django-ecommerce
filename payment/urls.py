from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_success, name='payment-success'),
    path('shipping-address/', views.checkout, name='shipping-address'),
    path('complete-order/', views.complete_order, name='complete-order'),
    path('process-payment/', views.process_payment, name='process-payment'),
    path('failed/', views.payment_failed, name='payment-failed'),
]
