from django import forms
from . import models
from django.forms import widgets

class CreateMeetForm(forms.ModelForm):

    class Meta():
        model = models.Meet
        fields = ('meet_name', 'date', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['date'].widget = forms.DateInput()
        self.fields['date'].widget = forms.SelectDateWidget()
