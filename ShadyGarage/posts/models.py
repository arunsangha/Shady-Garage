from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import auth

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
