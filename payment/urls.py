from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('success/', views.payment_success, name='payment-success'),
    path('failed/', views.payment_failed, name='payment-failed'),

]