from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import auth
from django.utils.text import slugify
from django.core.urlresolvers import reverse
#må legge til video og..
class Post(models.Model):
    user_fk = models.ForeignKey(User, related_name = "user_posting")
    post_title = models.CharField(max_length = 100)
    post_image = models.ImageField(upload_to="post_pic", blank = True)
    post_description = models.TextField(max_length = 255, blank = True)
    post_likes = models.ManyToManyField(auth.models.User, blank = True, related_name = "post_likes")
    post_created = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return "User:{} PostTitle: {}".format(self.user_fk.username, self.post_title)

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'slug':self.slug})

    def post_like(self):
        return reverse('posts:post_like', kwargs={'slug':self.slug})

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

class PostComment(models.Model):
     post_fk = models.ForeignKey(Post, related_name="post_comment_fk")
     user_fk = models.ForeignKey(User, related_name="post_comment_user")
     comment = models.TextField(max_length=1020)
     created = models.DateTimeField(auto_now_add = True)

     def __str__(self):
         return "Post: {} Kommentar:{}".format(self.post_fk.post_title, self.comment)
     class Meta:
         ordering = ['-created']
