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
        self.fields['instagram_profile'].label = "Instagram"
        self.fields['facebook_profile'].label = "Facebook"
        self.fields['description'].label = "Beskrivelse av klistremerke"
        self.fields['image'].label = "Eksempel bilde"
