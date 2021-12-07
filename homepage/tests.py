from django.test import TestCase

from .models import Art
class SwifriTests(TestCase):

    def test_check(self):
        art = Art.objects.first()
        self.assertIsNone(art)