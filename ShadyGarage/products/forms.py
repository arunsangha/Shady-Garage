from django import forms
from .models import CustomProduct

class CustomProductForm(forms.ModelForm):

    class Meta():
        model = CustomProduct
        fields = (
            'mobile',
            'instagram_profile',
            'facebook_profile',
            'description',
            'image',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mobile'].label = "Telefonnummer"
        self.fields['mobile'].widget.attrs.update({'placeholder': 'Påkrevd!'})
        self.fields['instagram_profile'].label = "Instagram"
        self.fields['instagram_profile'].widget.attrs.update({'placeholder': '@shadygarage.no'})
        self.fields['facebook_profile'].label = "Facebook"
        self.fields['facebook_profile'].widget.attrs.update({'placeholder': 'Shady Garage'})
        self.fields['description'].label = "Beskrivelse av klistremerke"
        self.fields['description'].widget.attrs.update({'placeholder': 'Påkrevd!'})
        self.fields['image'].label = "Eksempel bilde"
