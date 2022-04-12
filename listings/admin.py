from django.contrib import admin
from listings.models import Listing, ListingComment


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created', 'published')


class ListingCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created')


admin.site.register(Listing, ListingAdmin)
admin.site.register(ListingComment, ListingCommentAdmin)