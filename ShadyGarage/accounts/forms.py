from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models
class UserForm(UserCreationForm):

    class Meta():
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Brukernavn"
        self.fields["password1"].label = "Passord"
        self.fields["password2"].label = "Gjenta passord"

class ProfileForm(forms.ModelForm):
    class Meta():
        model = models.Profile
        fields = ("teams", "age", "profile_pic")

    def clean_image(self):
        image = self.cleaned_data.get('profile_pic', False)
        if image:
            if image._size > 4*700*700:
                raise ValidationError("Image file too large ( > 4mb )")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["teams"].label = "Team"
        self.fields["age"].label = "Alder"
        self.fields["profile_pic"].label = "Profilbilde"


class EditProfileForm(forms.ModelForm):
    class Meta():
        model = models.Profile
        fields = ('teams', 'age','profile_pic')

    def clean_image(self):
        image = self.cleaned_data.get('profile_pic', False)
        if image:
            if image._size > 4*700*700:
                raise ValidationError("Image file too large ( > 4mb )")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_pic'].label = "Profilbilde"
        self.fields['teams'].label = "Team"
        self.fields['age'].label = "Alder"
