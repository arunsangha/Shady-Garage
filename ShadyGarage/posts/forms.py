from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ('post_title', 'post_image', 'post_description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['post_title'].label = "Tittel"
        self.fields['post_image'].label = "Bilde"
        self.fields['post_description'].label = "Beskrivelse"

    def clean_image(self):
        image = self.cleaned_data.get('profile_pic', False)
        if image:
            if image._size > 4*700*700:
                raise ValidationError("Image file too large ( > 4mb )")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")

class PostCommentForm(forms.ModelForm):
    class Meta():
        model = models.PostComment
        fields = ('comment',)
