import os
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import auth
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
import piexif

class PostManager(models.Manager):
    def like_toggle(self, user, post_obj):
        if user in post_obj.post_likes.all():
            is_liked = True
            post_obj.post_likes.remove(user)
        else:
            Notification.objects.create(post_fk=post_obj, user_fk=user, owner=post_obj.user_fk, liked=True)
            is_liked = False
            post_obj.post_likes.add(user)
        return is_liked


class Post(models.Model):
    user_fk = models.ForeignKey(User, related_name = "user_posting")
    post_title = models.CharField(max_length = 100)
    post_image = models.ImageField(upload_to="post_pic", blank = True)
    thumbnail = models.ImageField(upload_to="thumbnail", blank=True)
    post_description = models.TextField(max_length = 255, blank = True)
    post_likes = models.ManyToManyField(auth.models.User, blank = True, related_name = "post_likes")
    post_created = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(unique = True)

    objects = PostManager()

    def __str__(self):
        return "User:{} PostTitle: {}".format(self.user_fk.username, self.post_title)

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'slug':self.slug})

    def _get_unique_slug(self):
        slug = slugify(self.post_title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}-{}'.format(slug, self.id, num)
            num += 1
        return unique_slug

    def create_thumbnail(self):
         from PIL import Image
         from io import BytesIO
         from django.core.files.uploadedfile import SimpleUploadedFile
         import os

        # Set our max thumbnail size in a tuple (max width, max height)
         THUMBNAIL_SIZE = (612, 612)

         DJANGO_TYPE = self.post_image.file.content_type

         if DJANGO_TYPE == 'image/jpeg':
             PIL_TYPE = 'jpeg'
             FILE_EXTENSION = 'jpg'
         elif DJANGO_TYPE == 'image/png':
             PIL_TYPE = 'png'
             FILE_EXTENSION = 'png'

        # Open original photo which we want to thumbnail using PIL's Image
         image = Image.open(BytesIO(self.post_image.read()))



         image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
         temp_handle = BytesIO()

         # Save exif tags from orignal image
         try:
             exif_dict=dict(image._getexif().items())
             image.save(temp_handle, PIL_TYPE, exif=exif_dict)
         except(AttributeError, KeyError, TypeError):
             image.save(temp_handle, PIL_TYPE)

         temp_handle.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into
        # ImageField
         suf = SimpleUploadedFile(os.path.split(self.post_image.name)[-1],
                 temp_handle.read(), content_type=DJANGO_TYPE)
        # Save SimpleUploadedFile into image field
         self.thumbnail.save(
             '%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION),
             suf,
             save=False
        )


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        if self.post_image:
            self.create_thumbnail()
        super().save()

    class Meta:
        ordering = ['-post_created']



class PostComment(models.Model):
     post_fk = models.ForeignKey(Post, related_name="post_comment_fk")
     user_fk = models.ForeignKey(User, related_name="post_comment_user")
     comment = models.TextField(max_length=1020)
     created = models.DateTimeField(auto_now_add = True)

     def __str__(self):
         return "Post: {} Kommentar:{}".format(self.post_fk.post_title, self.comment)
     class Meta:
         ordering = ['-created']

class PostCommentReply(models.Model):
    comment_fk = models.ForeignKey(PostComment, related_name="reply_comment_fk")
    user_fk = models.ForeignKey(User, related_name="reply_comment_user")
    comment = models.TextField(max_length=1020)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "PostComment: {} Reply: {}".format(self.comment_fk.comment, self.comment)


class NotificationManager(models.Manager):
    def seen_toggle(self, user, notification_obj):
        if notification_obj.seen == True:
            is_seen = True
        else:
            is_seen = False
            notification_obj.seen = True
            notification_obj.save()
        return is_seen

class Notification(models.Model):
    post_fk = models.ForeignKey(Post, related_name="post_notification_fk")
    user_fk = models.ForeignKey(User, related_name="post_notification_user")
    noti_fk = models.ForeignKey(PostComment, related_name="notiii", blank=True, null=True)
    noti_reply_fk = models.ForeignKey(PostCommentReply, related_name="notiii_reply", blank=True, null=True)
    owner = models.ForeignKey(User, related_name="post_notification_owner")
    commented = models.BooleanField(default=False, blank=True)
    liked = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False, blank=True)

    objects = NotificationManager()

    def __str__(self):
        return "PostOwner: {}, Seen:{}".format(self.owner, self.seen)

    class Meta:
        ordering = ['-created']

from PIL import Image, ExifTags
def rotate_image(filepath, thumbnail_filepath):
  rotation = 0
  try:
    image = Image.open(filepath)
    for orientation in ExifTags.TAGS.keys():
      if ExifTags.TAGS[orientation] == 'Orientation':
            break
    exif = dict(image._getexif().items())

    if exif[orientation] == 3:
        image = image.rotate(180, expand=True)
        rotation = 180
    elif exif[orientation] == 6:
        image = image.rotate(270, expand=True)
        rotation = 270
    elif exif[orientation] == 8:
        image = image.rotate(90, expand=True)
        rotation = 90
    image.save(filepath)
    image.close()

    image = Image.open(thumbnail_filepath)
    image = image.rotate(rotation, expand=True)
    image.save(thumbnail_filepath)
    image.close()
    rotation = 0
  except (AttributeError, KeyError, IndexError):
    # cases: image don't have getexif
    pass

@receiver(post_save, sender=Post, dispatch_uid="update_image_profile")
def update_image(sender, instance, **kwargs):
  if instance.post_image:
      BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
      fullpath = BASE_DIR + instance.post_image.url
      fullpath_thumbnail = BASE_DIR + instance.thumbnail.url
      rotate_image(fullpath, fullpath_thumbnail)

@receiver(post_save, sender=PostComment)
def create_notification(sender, instance, **kwargs):
    if(kwargs.get('created', False)):
        user_fk = instance.user_fk
        post_fk = instance.post_fk
        owner = instance.post_fk.user_fk
        Notification.objects.create(post_fk=post_fk, user_fk=user_fk, noti_fk=instance, owner=owner, commented=True)

@receiver(post_save, sender=PostCommentReply)
def create_notification_reply(sender, instance, **kwargs):
    if(kwargs.get('created', False)):
        Notification.objects.create(post_fk=instance.comment_fk.post_fk, user_fk=instance.user_fk, noti_reply_fk=instance, owner=instance.comment_fk.user_fk)
