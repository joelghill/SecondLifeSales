from django.test import TestCase, Client
from django.urls import reverse

from profiles.models import Profile


class CreateProfileViewTestCase(TestCase):

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

        client = Client()

        url = reverse('register')
        response = client.post(path=url, data=data)

        self.assertEqual(response.status_code, 302)

        profile: Profile = Profile.objects.first()

        self.assertEqual(profile.country, country)
        self.assertEqual(profile.city, city)
        self.assertEqual(profile.province_state, province)