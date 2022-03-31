from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView


class CreateProfileView(FormView):

    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = "registration/register.html"