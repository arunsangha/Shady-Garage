from django import forms
from . import models

class Entertainment(forms.ModelForm):
    class Meta():
        model = models.Entertainment
        fields = ('title', 'image', 'youtube_link',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "Title"
        self.fields['image'].label = "Bilde"
        self.fields['youtube_link'].lable = "Youtube Link"
