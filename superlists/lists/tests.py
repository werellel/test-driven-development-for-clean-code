from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):
	def test_bad_maths(self):
		self.assertEqual(1 + 1, 3)


# from django.core.urlresolvers import resolve
from django.urls import reverse
from lists.views import home_page # 1

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = reverse('/') # 2
		self.assertEqual(found.func, home_page) # 3