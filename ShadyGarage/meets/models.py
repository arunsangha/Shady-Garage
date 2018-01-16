from django.db import models
from django.contrib import auth
from django.utils.text import slugify
from django.core.urlresolvers import reverse
# Create your models here.
class Meet(models.Model):

    meet_name = models.CharField(max_length = 200, unique = True)
    date = models.DateTimeField()
    time = models.TimeField(blank = True, default="19:00:00")
    slug = models.SlugField(allow_unicode = True, unique = True)
    description = models.TextField()
    meet_image = models.ImageField(upload_to = "meets_pic", blank = True, default = "/meets_pic/meet_default.png")
    users_joining = models.ManyToManyField(auth.models.User, blank = True, related_name = "members_joining_meet")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.meet_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("meets:single", kwargs={"slug":self.slug})

    def join_url(self):
        return reverse("meets:join_meet", kwargs={"slug":self.slug})
