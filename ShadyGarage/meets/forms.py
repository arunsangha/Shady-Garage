from django import forms
from . import models
from django.forms import widgets
from django.forms import MultiWidget
import datetime

class CreateMeetForm(forms.ModelForm):

    class Meta():
        model = models.Meet
        fields = ('meet_name', 'description', 'category', 'date', 'time','location', 'marker_image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['meet_name'].label = "Treff navn"
        self.fields['date'].widget = widgets.SelectDateWidget()
        self.fields['date'].initial = datetime.date.today()
        self.fields['date'].label = "Dato"
        self.fields['time'].label = "Treffet starter..."
        self.fields['description'].label = "Beskrivelse av treffet:"
        self.fields['location'].label = "Adresse:"
        self.fields['location'].widget.attrs.update({'placeholder': 'F.eks "Altagårdskogen 32, 9515 Alta"'})
        self.fields['marker_image'].label = "Markør på kart:"
        self.fields['category'].label = "Kategori"

class CommentForm(forms.ModelForm):
    class Meta():
        model = models.Meet_Comment
        fields = ('comment',)
