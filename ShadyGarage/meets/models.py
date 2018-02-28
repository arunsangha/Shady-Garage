from django.db import models
from django.contrib import auth
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import auth
# Create your models here.

class MeetManager(models.Manager):
    def join_toggle(self, user, meet_obj):
        if user in meet_obj.users_joining.all():
            is_joining = True
            meet_obj.users_joining.remove(user)
        else:
            is_joining = False
            meet_obj.users_joining.add(user)

        return is_joining

class Meet(models.Model):
    user_fk = models.ForeignKey(auth.models.User, related_name="meets_user_fk")
    meet_name = models.CharField(max_length = 255, unique = True)
    date = models.DateTimeField()
    time = models.TimeField(blank = True, default="19:00:00")
    slug = models.SlugField(allow_unicode = True, unique = True)
    description = models.TextField()
    meet_image = models.ImageField(upload_to = "meets_pic", blank = True, default = "/meets_pic/meet_default.png")
    users_joining = models.ManyToManyField(auth.models.User, blank = True, related_name = "members_joining_meet")
    location = models.CharField(max_length = 1275)
    objects = MeetManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.meet_name)
        super().save()

    def get_absolute_url(self):
        return reverse("meets:single", kwargs={"slug":self.slug})

    def join_url(self):
        return reverse("meets:join_meet", kwargs={"slug":self.slug})

    def __str__(self):
        return str(self.meet_name)

    class Meta:
        ordering = ['date']

class Meet_Comment(models.Model):
    meet_fk = models.ForeignKey(Meet, related_name="meet_comment")
    user = models.ForeignKey(User, related_name="meet_comment_user")
    comment = models.TextField(max_length = 255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "Treff:{} | Kommentar : {}".format(self.meet_fk.meet_name, self.comment)
