from django.views.generic import ListView, DetailView
from listings.models import Listing


class ListingsListView(ListView):
    model = Listing
    
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ListingDetailView(DetailView):
    model = Listing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context