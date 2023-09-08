from django.contrib import admin
from .models import ShippingAddress, Order, OrderedItem

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderedItem)
