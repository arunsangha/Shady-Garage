from django.db import models
from django.contrib import auth
# Create your models here.

class Entertainment(models.Model):
    user_fk = models.ForeignKey(auth.models.User, related_name="entertainment_user")
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="entertainment_pic/%Y/%M/%D/", blank=True)
    youtube_link = models.CharField(max_length=255, blank=True)
