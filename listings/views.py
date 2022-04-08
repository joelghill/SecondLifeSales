from django.views.generic import ListView, DetailView, TemplateView
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


class ListingsHomeView(TemplateView):

    template_name = "listings/listings_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["listings"] = self.get_listings()

        return context

    def get_listings(self):
        return Listing.objects.filter(published=True)