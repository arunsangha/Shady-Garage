from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse



class Car(models.Model):
    make                 = models.CharField(max_length=20)
    model                = models.CharField(max_length=20)
    price                = models.CharField(max_length=40)
    engine               = models.CharField(max_length=50)
    zero_to_100          = models.DecimalField(max_digits=5, decimal_places=1)
    consumption          = models.DecimalField(max_digits=5, decimal_places=1)

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
    intro_image          = models.ImageField(upload_to="blogs/intro_image")
    intro_title          = models.CharField(max_length=70)
    intro_paragraph      = models.CharField(max_length=600)
    gif                  = models.ImageField(upload_to="blogs/gif")
    paragraph_one_title  = models.CharField(max_length=70)
    paragraph_one        = models.CharField(max_length=2000)
    youtube_link         = models.CharField(max_length=1000)
    first_parallax       = models.ImageField(upload_to="blogs/parallax_1")
    paragraph_two_title  = models.CharField(max_length=70)
    paragraph_two        = models.CharField(max_length=2000)
    paragraph_two_image  = models.ImageField(upload_to="blogs/paragraph_3")
    second_parallax        = models.ImageField(upload_to="blogs/parallax_2")
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = _get_unique_slug()

        super().save()
