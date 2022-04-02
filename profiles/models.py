from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    handle = models.CharField(max_length=120, blank=True)

    # Contact Info
    phone_number = models.CharField(max_length=20, blank=True)

    # Location
    country = models.CharField(max_length=120, blank=False)
    province_state = models.CharField(max_length=250, blank=False)
    postal_zip = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=250, blank=False)

    # TODO: Credit card or payment info?
    

