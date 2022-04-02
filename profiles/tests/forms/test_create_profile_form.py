from django.test import TestCase, Client

from profiles.forms import CreateUserProfileForm
from profiles.models import Profile


class CreateUserProfileFormTestCase (TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_create_user(self):

        first_name = "Joel"
        last_name = "Hill"
        email = "fake@email.com"
        username = "joelh"

        country = "Canada"
        province = "SK"
        city = "Stoon"
        postal_code = "s7k3a4"

        password1 = "ThisIsATestPassword!123"
        password2 = "ThisIsATestPassword!123"

        data = {
            "first_name": "Joel",
            "last_name": "Hill",
            "email": "fake@email.com",
            "username": "joelh",

            "country": "Canada",
            "province": "SK",
            "city": "Stoon",
            "postal_code": "s7k3a4",

            "password1": "ThisIsATestPassword!123",
            "password2": "ThisIsATestPassword!123"
        }

        form = CreateUserProfileForm(data=data)
        is_valid = form.is_valid()

        self.assertTrue(is_valid)

        form.save()

        profile: Profile = Profile.objects.first()
        print(Profile.objects.count())

        self.assertEqual(profile.country, country)
        self.assertEqual(profile.city, city)
        self.assertEqual(profile.province_state, province)
