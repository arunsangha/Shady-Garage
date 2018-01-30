import itertools
from django import forms
from . import models
from django.utils.text import slugify

class PostForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ('post_title', 'post_image', 'post_description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['post_title'].label = "Tittel"
        self.fields['post_image'].label = "Bilde"
        self.fields['post_description'].label = "Beskrivelse"

    def save(self):
        instance = super(PostForm, self).save(commit=False)
        max_length = models.Post._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.post_title)[:max_length]

        for x in itertools.count(1):
            if not models.Post.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig[:max_length - len(str(x))-1], x)

        instance.save()

        return instance
