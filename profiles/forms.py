from cProfile import label
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext, gettext_lazy as _

from profiles.models import Profile


class CreateUserProfileForm(UserCreationForm):

    first_name = forms.CharField(label=_("First Name"), max_length=50, required=True)
    last_name = forms.CharField(label=_("Last Name"), max_length=50, required=True)

    # Contact information
    email = forms.EmailField(label=_("Email"), required=True)
    phone_number = forms.CharField(
        label=_("Phone Number"), max_length=20, required=False
    )

    # Address
    country = forms.CharField(label=_("Country"), required=True)
    province = forms.CharField(label=_("Province/State"), required=True)
    city = forms.CharField(label=_("City"), required=True)
    postal_code = forms.CharField(label=_("Postal/Zip Code"), required=True)

    def save(self, commit=True):

        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.email = self.cleaned_data.get("email")

        profile = Profile(
            phone_number=self.cleaned_data.get("phone_number"),
            country=self.cleaned_data.get("country"),
            province_state=self.cleaned_data.get("province"),
            postal_zip=self.cleaned_data.get("postal_code"),
            city=self.cleaned_data.get("city"),
        )

        if commit:
            user.save()

            profile.user = user
            profile.save()

        return user
