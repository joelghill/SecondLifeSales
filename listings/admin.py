from django.contrib import admin
from listings.models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created', 'published')

admin.site.register(Listing, ListingAdmin)