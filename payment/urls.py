from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_success, name='payment-success'),
    path('process-payment/', views.checkout, name='process-payment'),
    path('complete-order/', views.complete_order, name='complete-order'),
    path(
        'registered-user-checkout/',
        views.registered_user_checkout,
        name='registered-user-checkout',
    ),
    path('failed/', views.payment_failed, name='payment-failed'),
]
