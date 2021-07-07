from django.test import TestCase

# Create your tests here.
# class SmokeTest(TestCase):
# 	def test_bad_maths(self):
# 		self.assertEqual(1 + 1, 3)


# from django.core.urlresolvers import resolve
from django.urls import reverse
from lists.views import home_page # 1
from django.http import HttpRequest

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = reverse('/') # 2
		self.assertEqual(found.func, home_page) # 3


	def test_home_page_returns_correct_html(self):
		request = HttpRequest() # 1
		response = home_page(request) # 2
		self.assertTrue(response.content.startswith(b'<html>')) # 3
		self.assertIn(b'<title>To-Do lists</title>', response.content) # 4
		self.assertTrue(response.content.endswith(b'</html>')) # 5

	def test_home_page_can_save_a_POST_request(self):
	    request = HttpRequest()
	    request.method = 'POST'
	    request.POST['item_text'] = '신규 작업 아이템'
	    response = home_page(request)
	    
	    self.assertIn('신규 작업 아이템', response.content.decode())