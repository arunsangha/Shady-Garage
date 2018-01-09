from django.db import models
from django.contrib import auth
from django.db.models.signals import post_save
# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

class Profile(models.Model):
    user = models.OneToOneField(auth.models.User, on_delete = models.CASCADE)
    teams = models.CharField(max_length = 150)
    age = models.PositiveIntegerField(null = True, blank = True)
    profile_pic = models.ImageField(upload_to = "profile_pic", default = "/default/default.png")

def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(users = kwargs['instance'])

post_save.connect(create_profile, sender = User)
