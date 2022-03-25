from django.urls import path
from listings.views import ListingsListView

urlpatterns = [
    path('', ListingsListView.as_view(), name='listings_list'),
]