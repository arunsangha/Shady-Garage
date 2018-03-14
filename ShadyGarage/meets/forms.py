from django import forms
from . import models
from django.forms import widgets

class CreateMeetForm(forms.ModelForm):

    class Meta():
        model = models.Meet
        fields = ('meet_name', 'description','date', 'time','location', 'marker_image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['meet_name'].label = "Treff navn"
        self.fields['date'].widget = widgets.SelectDateWidget()
        self.fields['date'].label = "Dato"
        self.fields['time'].label = "Treffet starter..."
        self.fields['description'].label = "Beskrivelse av treffet:"
        self.fields['location'].label = "Adresse:"
        self.fields['location'].widget.attrs.update({'placeholder': 'F.eks "Altagårdskogen 32, 9515 Alta"'})
        self.fields['marker_image'].label = "Markør på kart:"

class CommentForm(forms.ModelForm):
    class Meta():
        model = models.Meet_Comment
        fields = ('comment',)
