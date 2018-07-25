from django import forms
from . import models
from django.forms import widgets
from django.forms import MultiWidget
import datetime

class CreateMeetForm(forms.ModelForm):
    class Meta():
        model = models.Meet
        fields = ('organizer', 'anonymous', 'meet_name', 'description','category', 'date', 'time','location', 'marker_image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['organizer'].label = "Arrangør"
        self.fields['organizer'].widget.attrs.update({'placeholder': 'Anonym? Marker knappen under'})
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
        self.fields['anonymous'].label = "Anonym"

class CommentForm(forms.ModelForm):
    class Meta():
        model = models.Meet_Comment
        fields = ('comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].label = "Kommentar:"
        self.fields['comment'].widget.attrs.update({'placeholder': 'F.eks: Hva slags biler kommer folk med? :D'})

class AdminMessageForm(forms.ModelForm):
    class Meta():
        model = models.MeetAdminMessage
        fields = ('message',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].label = "Melding"
