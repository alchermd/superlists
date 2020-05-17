from django.test import TestCase

class HomePageTest(TestCase):
	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'lists/home.html')

	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'body': 'Buy some eggs.'})
		self.assertIn('Buy some eggs.', response.content.decode())
		self.assertTemplateUsed(response, 'lists/home.html')