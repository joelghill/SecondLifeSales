from email.policy import default
from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self) -> str:
        user: User = self.owner.user
        return f"{user.first_name} {user.last_name}: {self.title}"


class ListingComment(models.Model):

    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=False, related_name="comments")

    text = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        user: User = self.author.user
        return f"{self.author.pk}: {user.first_name} {user.last_name}: {self.text[0 : 25]}"