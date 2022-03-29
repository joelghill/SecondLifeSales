from email.policy import default
from django.db import models

from profiles.models import Profile


class Listing(models.Model):

    # Text Descriptions
    title = models.CharField(max_length=250)
    description = models.TextField()

    # Pricing 
    price = models.FloatField()
    price_fixed = models.BooleanField(default=False)

    # Publication 
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    # Image
    image = models.ImageField(default=None)

    # Owner
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
