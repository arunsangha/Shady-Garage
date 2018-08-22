from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta():
        model = Address
        fields = (
                'address_line_1',
                'post_code',
                'city',
                'country',
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address_line_1'].label = "Addresse"
        self.fields['post_code'].label = "Postkode"
        self.fields['city'].label = "By"
        self.fields['country'].label = "Land"
