from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta():
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Brukernavn"
        self.fields["password1"].label = "Passord"
        self.fields["password2"].label = "Gjenta passord"
