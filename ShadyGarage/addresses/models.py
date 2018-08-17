from django.db import models
from billing.models import BillingProfile
# Create your models here.

ADDRESS_TYPE = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)

class Address(models.Model):
    user            = models.ForeignKey(BillingProfile, related_name="billing_profile_address")
    address_type    = models.CharField(choices=ADDRESS_TYPE, max_length=120)
    address_line_1  = models.CharField(max_length=120)
    city            = models.CharField(max_length=120)
    post_code       = models.CharField(max_length=40)
    country         = models.CharField(max_length=120, default="Norge")

    def __str__(self):
        return "{username}: {adr_type}".format(
                username=self.user.username,
                adr_type=self.adr_type,
            )

    def get_address(self):
        return "{line1}, {line2} {line4}".format(
            line1 = self.address_line_1,
            line2 = self.post_code,
            line3 = self.city,
        )
