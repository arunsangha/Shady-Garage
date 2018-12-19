from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from ShadyGarage.utils import rotate_image
import os

engine_choices = (
    ('V12', 'V12'),
    ('V10', 'V10'),
    ('V8', 'V8'),
    ('V6', 'V6'),
    ('R5', 'R5'),
    ('R4', 'R4'),
    ('R3', 'R3'),
)

drive_train_choices = (
    ('4WD', 'Firehjulsdrift'),
    ('FWD', 'Forhjulsdrift'),
    ('RWD', 'Bakhjulsdrift'),
)

class Car(models.Model):
    make                 = models.CharField(max_length=20)
    model                = models.CharField(max_length=20)
    price                = models.PositiveIntegerField(default=0)
    hp                   = models.PositiveIntegerField(default=10)
    nm                   = models.PositiveIntegerField(default=10)
    engine               = models.CharField(choices=engine_choices, max_length=50)
    liter                = models.DecimalField(max_digits=5, decimal_places=1)
    zero_to_100          = models.DecimalField(max_digits=5, decimal_places=1)
    consumption          = models.DecimalField(max_digits=5, decimal_places=1)
    drive_train          = models.CharField(choices=drive_train_choices, max_length=10)

    def get_price(self):
        price = str(self.price)
        if self.price < 1000000:
            return "{}.{} kr".format(price[0:3], price[3:])
        return "{} {} {} kr".format(price[0:1], price[1:4], price[4:7])

    def get_engine(self):
        return "{}L {}".format(self.liter, self.engine)

    def __str__(self):
        return "{}-{}".format(self.make, self.model)

class UserVote(models.Model):
    car  = models.ForeignKey(Car, related_name="car_vote_fk")
    vote = models.NullBooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {} {}".format(self.car.model, self.vote, self.timestamp)

class Blog(models.Model):
    car                  = models.ForeignKey(Car, related_name="car_fk")
    title                = models.CharField(max_length=200)
    top_image            = models.ImageField(upload_to="blogs/top_image")
    top_image_mobile     = models.ImageField(upload_to="blogs/mobile/top_image",blank=True, null=True)
    intro_image          = models.ImageField(upload_to="blogs/intro_image")
    intro_image_mobile   = models.ImageField(upload_to="blogs/mobile/intro_image", blank=True, null=True)
    intro_title          = models.CharField(max_length=70)
    intro_paragraph      = models.CharField(max_length=600)
    gif                  = models.ImageField(upload_to="blogs/gif")
    paragraph_one_title  = models.CharField(max_length=70)
    paragraph_one        = models.CharField(max_length=2000)
    youtube_link         = models.CharField(max_length=1000)
    first_parallax       = models.ImageField(upload_to="blogs/parallax_1")
    first_parallax_mobile = models.ImageField(upload_to="blogs/mobile/parallax_1",blank=True, null=True)
    paragraph_two_title  = models.CharField(max_length=70)
    paragraph_two        = models.CharField(max_length=2000)
    paragraph_two_image  = models.ImageField(upload_to="blogs/paragraph_3")
    paragraph_two_image_mobile  = models.ImageField(upload_to="blogs/mobile/paragraph_3",blank=True, null=True)
    second_parallax        = models.ImageField(upload_to="blogs/parallax_2")
    second_parallax_mobile = models.ImageField(upload_to="blogs/mobile/parallax_2",blank=True, null=True)
    paragraph_three_title  = models.CharField(max_length=70)
    paragraph_three        = models.CharField(max_length=2000)
    score                  = models.PositiveIntegerField()
    slug                   = models.SlugField(unique=True)

    def __str__(self):
        return "{}".format(self.title)

    def _get_unique_slug(self):
        slug = slugify("sg:"+self.title)
        unique_slug = slug
        num = 1
        id=self.id
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}-{}'.format(slug, id, num)
            num += 1
        return unique_slug

    def get_absolute_url(self):
        return reverse('blogs:detail', kwargs={'slug':self.slug})

    def get_class(self):
        return self.__class__.__name__

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = _get_unique_slug()

        super().save()

@receiver(post_save, sender=Blog, dispatch_uid="update_image_blog")
def update_image(sender, instance, **kwargs):
  if instance.top_image_mobile and instance.intro_image_mobile and instance.paragraph_two_image and instance.first_parallax_mobile and instance.second_parallax_mobile:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.top_image_mobile.url
    rotate_image(fullpath)
    fullpath = BASE_DIR + instance.intro_image_mobile.url
    rotate_image(fullpath)
    fullpath = BASE_DIR + instance.paragraph_two_image.url
    rotate_image(fullpath)
    fullpath = BASE_DIR + instance.first_parallax_mobile.url
    rotate_image(fullpath)
    fullpath = BASE_DIR + instance.second_parallax_mobile.url
    rotate_image(fullpath)
