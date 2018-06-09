from django.db import models
from django.contrib import auth
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

class Profile(models.Model):
    TEAM_CHOICES = (('SHADYGARAGE', "ShadyGarage"), ('CLASSIC', "Classic"), ('OFFROAD', "Offroad"), ('STANCE', "Stance"), ('TUNER', "Tuner"), ('MC', "MC"))
    user = models.OneToOneField(auth.models.User, on_delete = models.CASCADE)
    teams = models.CharField(max_length = 50, choices = TEAM_CHOICES, default="SHADYGARAGE")
    age = models.PositiveIntegerField(null = True, blank = True)
    profile_pic = models.ImageField(upload_to = "profile_pic", default = "default/default.png")
    thumbnail = models.ImageField(upload_to="profile_pic_thumbnail", default ="default/default.png")
    def __str__(self):
        return self.user.username

    def create_thumbnail(self):
         from PIL import Image
         from io import BytesIO
         from django.core.files.uploadedfile import SimpleUploadedFile
         import os

        # Set our max thumbnail size in a tuple (max width, max height)
         THUMBNAIL_SIZE = (612, 612)


         DJANGO_TYPE = self.profile_pic.file.content_type

         if DJANGO_TYPE == 'image/jpeg':
             PIL_TYPE = 'jpeg'
             FILE_EXTENSION = 'jpg'
         elif DJANGO_TYPE == 'image/png':
             PIL_TYPE = 'png'
             FILE_EXTENSION = 'png'

        # Open original photo which we want to thumbnail using PIL's Image
         image = Image.open(BytesIO(self.profile_pic.read()))

         image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
         temp_handle = BytesIO()
         image.save(temp_handle, PIL_TYPE)
         temp_handle.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into
        # ImageField
         suf = SimpleUploadedFile(os.path.split(self.profile_pic.name)[-1],
                 temp_handle.read(), content_type=DJANGO_TYPE)
        # Save SimpleUploadedFile into image field
         self.thumbnail.save(
             '%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION),
             suf,
             save=False
        )

    def save(self, *args, **kwargs):
        if self.profile_pic:
            if self.profile_pic != 'default/default.png':
                self.create_thumbnail()

        super().save()

@receiver(post_save, sender=auth.models.User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, teams="SHADYGARAGE")
