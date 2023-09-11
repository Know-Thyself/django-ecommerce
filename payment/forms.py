from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name not in ['state', 'zipcode']:
                visible.field.widget.attrs['class'] = 'form-control required'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = ShippingAddress
        fields = [
            'full_name',
            'email',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
        ]
        exclude = [
            'user',
        ]
        labels = {
            "full_name": 'Full Name',
            'email': 'Email',
            'address1': 'First Line of Your Address',
            'address2': 'Second Line of Your Address',
            'city': 'City',
            'state': 'State or Province',
            'zipcode': 'Zipcode',
        }
