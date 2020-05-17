from django.test import TestCase

from .models import Item

class HomePageTest(TestCase):
	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'lists/home.html')

	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'body': 'Buy some eggs.'})

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'Buy some eggs.')

	def test_redirects_after_POST(self):
		response = self.client.post('/', data={'body': 'Buy some eggs.'})
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_only_saves_item_when_necessary(self):
		self.client.get('/')
		self.assertEquals(Item.objects.count(), 0)

	def test_displays_all_items(self):
		Item.objects.create(text='Item 1')
		Item.objects.create(text='Item 2')

		response = self.client.get('/')

		self.assertIn('Item 1', response.content.decode())
		self.assertIn('Item 2', response.content.decode())

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