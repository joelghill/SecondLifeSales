from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView

from profiles.forms import CreateUserProfileForm


class CreateProfileView(FormView):

    form_class = CreateUserProfileForm
    success_url = reverse_lazy('home')
    template_name = "registration/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)