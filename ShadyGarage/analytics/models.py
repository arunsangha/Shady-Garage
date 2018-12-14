from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
User = get_user_model()

class ObjectViewed(models.Model):
    user            = models.ForeignKey(User, blank=True, null=True)
    ip_address      = models.CharField(max_length=220, blank=True, null=True)
    content_type    = models.ForeignKey(ContentType)
    object_id       = models.PositiveIntegerField()
    content_object  = GenericForeignKey('content_type', 'object_id')
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Viewed-{}-{}".format(self.content_type, self.content_object)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Object viewed"
        verbose_name_plural = "Objects viewed"
