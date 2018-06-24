from django.db import models
from django.contrib import auth
# Create your models here.

class Entertainment(models.Model):
    user_fk = models.ForeignKey(auth.models.User, related_name="entertainment_user")
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="entertainment_pic/%Y/%M/%D/", blank=True)
    youtube_link = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return "{}".format(self.id)

    def save(self, *args, **kwargs):
        if self.image:
            self.create_thumbnail()
        super().save()

    def create_thumbnail(self):
         from PIL import Image
         from io import BytesIO
         from django.core.files.uploadedfile import SimpleUploadedFile
         import os

        # Set our max thumbnail size in a tuple (max width, max height)
         THUMBNAIL_SIZE = (612, 612)

         DJANGO_TYPE = self.image.file.content_type

         if DJANGO_TYPE == 'image/jpeg':
             PIL_TYPE = 'jpeg'
             FILE_EXTENSION = 'jpg'
         elif DJANGO_TYPE == 'image/png':
             PIL_TYPE = 'png'
             FILE_EXTENSION = 'png'

        # Open original photo which we want to thumbnail using PIL's Image
         image = Image.open(BytesIO(self.image.read()))



         image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
         temp_handle = BytesIO()


         image.save(temp_handle, PIL_TYPE)

         temp_handle.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into
        # ImageField
         suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                 temp_handle.read(), content_type=DJANGO_TYPE)
        # Save SimpleUploadedFile into image field
         self.image.save(
             '%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION),
             suf,
             save=False
        )

    class Meta:
        ordering = ['-created']
