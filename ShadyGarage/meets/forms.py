from django import forms
from . import models
from django.forms import widgets

class CreateMeetForm(forms.ModelForm):

    class Meta():
        model = models.Meet
        fields = ('meet_name', 'date', 'time', 'description', 'latitude', 'longitude')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['meet_name'].label = "Treff navn"
        self.fields['date'].widget = widgets.SelectDateWidget()
        self.fields['date'].label = "Dato"
        self.fields['time'].label = "Treffet starter..."
        self.fields['description'].label = "Beskrivelse av treffet:"

class CreateMeetComment(forms.ModelForm):
    class Meta():
        model = models.Meet_comments
        fields = ('comment',)
