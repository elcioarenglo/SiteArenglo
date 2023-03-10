from django.test import TestCase
from django.urls import reverse

class ArengloURLsTest(TestCase):

    def test_arenglo_home_url_is_correct(self):
        home_url = reverse('home')
        self.assertEqual(home_url, '/')