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
    post_likes = models.ManyToManyField(auth.models.User, blank = True, related_name = "post_likes" )
    slug = models.SlugField(unique = True)

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
