from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import auth
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    class Meta:
        ordering = ['-post_created']



#//TODO:Reply for comments. Gjelder for meets og.

class PostComment(models.Model):
     post_fk = models.ForeignKey(Post, related_name="post_comment_fk")
     user_fk = models.ForeignKey(User, related_name="post_comment_user")
     comment = models.TextField(max_length=1020)
     created = models.DateTimeField(auto_now_add = True)

     def __str__(self):
         return "Post: {} Kommentar:{}".format(self.post_fk.post_title, self.comment)
     class Meta:
         ordering = ['-created']

class Notification(models.Model):
    post_fk = models.ForeignKey(Post, related_name="post_notification_fk")
    user_fk = models.ForeignKey(User, related_name="post_notification_user")
    noti_fk = models.ForeignKey(PostComment, related_name="notiii", blank=True, null=True)
    owner = models.ForeignKey(User, related_name="post_notification_owner")
    commented = models.BooleanField(default=False, blank=True)
    liked = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

@receiver(post_save, sender=PostComment)
def create_notification(sender, instance, **kwargs):
    if(kwargs.get('created', False)):
        user_fk = instance.user_fk
        post_fk = instance.post_fk
        owner = instance.post_fk.user_fk
        Notification.objects.create(post_fk=post_fk, user_fk=user_fk, noti_fk=instance, owner=owner, commented=True)
