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

    
class PostCommentForm(forms.ModelForm):
    class Meta():
        model = models.PostComment
        fields = ('comment',)

class PostCommentReplyForm(forms.ModelForm):
    class Meta():
        model = models.PostCommentReply
        fields = ('comment',)
