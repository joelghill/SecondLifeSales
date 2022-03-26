from django.urls import path

from listings.views import ListingsListView, ListingDetailView

urlpatterns = [
    path('', ListingsListView.as_view(), name='listings_list'),
    path('<slug:pk>', ListingDetailView.as_view(), name='listing_details'),
]