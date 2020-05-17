from django.test import TestCase

from .models import Item

class HomePageTest(TestCase):
	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'lists/home.html')

	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'body': 'Buy some eggs.'})
		self.assertIn('Buy some eggs.', response.content.decode())
		self.assertTemplateUsed(response, 'lists/home.html')

class ItemModelTest(TestCase):
	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'My first item'
		first_item.save()

		second_item = Item()
		second_item.text = 'My second item'
		second_item.save()

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'My first item')
		self.assertEqual(second_saved_item.text, 'My second item')