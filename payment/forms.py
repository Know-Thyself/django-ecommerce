from django import forms
from .models import ShippingAddressModel


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddressModel
        fields = [
            'full_name',
            'email',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
        ]
        exclude = ['user',]