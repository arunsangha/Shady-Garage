from django import forms
from . import models
from django.forms import widgets
from django.forms import MultiWidget
import datetime

class CreateMeetForm(forms.ModelForm):
    class Meta():
        model = models.Meet
        fields = ('organizer','meet_name', 'description','date', 'time', 'adress', 'post_code', 'city', 'meet_image','marker_image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['organizer'].label = "Arrangør"
        self.fields['organizer'].widget.attrs.update({'placeholder': 'Crew Navn'})
        self.fields['meet_name'].label = "Treff navn"
        self.fields['date'].widget = widgets.SelectDateWidget()
        self.fields['date'].initial = datetime.date.today()
        self.fields['date'].label = "Dato"
        self.fields['time'].label = "Treffet starter..."
        self.fields['description'].label = "Beskrivelse av treffet:"
        self.fields['adress'].label = "Adresse:"
        self.fields['adress'].widget.attrs.update({'placeholder': 'F.eks "Altagårdskogen 32"'})
        self.fields['marker_image'].label = "Markør på kart:"

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
