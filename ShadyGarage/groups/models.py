from django.db import models
from django.utils.text import slugify
# Create your models here.
import misaka
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

#slugify tillater mellomrom fra input men fjerner de når det lagres til db
# antar for å spare plass?

#misaka tillater markdown text, usikker på hva det betyr

class Group(models.Model):
    name = models.CharField(max_length=255, unique = True)
    slug = models-slugField(allow_unicode = True, unique = True)
    description = models.TextField(blank = True, default = "")
    description_html = models.TextField(editable = False, default = '', blank = True)
    members = models.ManyToManyField(User, through = 'GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs = {'slug' : self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    # Linking table mellom gruppe og user
    group = models.ForeignKey(Group, related_name = 'memberships')
    user = models.ForeignKey(User, related_name = 'user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        # Sammensatt primærnøkkel
        unique_together = ('group', 'user')
