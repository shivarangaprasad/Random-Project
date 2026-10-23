from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    @patch("random_console.views.randint", side_effect=[42, 0xABCDEF])
    def test_home_displays_number_and_color(self, _randint):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, ">42<")
        self.assertContains(response, "#ABCDEF")

