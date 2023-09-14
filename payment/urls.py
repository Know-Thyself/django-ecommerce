from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='process-payment'),
    path('success/', views.payment_success, name='payment-success'),
    path(
        'checkout/',
        views.registered_user_checkout,
        name='registered-user-checkout',
    ),
    path('failed/', views.payment_failed, name='payment-failed'),
    path('track-orders/', views.track_orders, name='track-orders')
]
