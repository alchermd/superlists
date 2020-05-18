from django.test import TestCase

from .models import Item, List

class HomePageTest(TestCase):
	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'lists/home.html')

class ListAndItemModelTest(TestCase):
	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = 'My first item'
		first_item.list = list_
		first_item.save()

		second_item = Item()
		second_item.text = 'My second item'
		second_item.list = list_
		second_item.save()

		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		self.assertEqual(first_saved_item.text, 'My first item')
		self.assertEqual(first_saved_item.list, list_)

		second_saved_item = saved_items[1]
		self.assertEqual(second_saved_item.list, list_)
		self.assertEqual(second_saved_item.text, 'My second item')

class ListViewTest(TestCase):
	def test_uses_list_template(self):
		list_ = List.objects.create()
		response = self.client.get(f'/lists/{list_.id}/')
		self.assertTemplateUsed(response, 'lists/list.html')

	def test_displays_only_items_for_that_list(self):
		correct_list = List.objects.create()
		Item.objects.create(text='Item 1', list=correct_list)
		Item.objects.create(text='Item 2', list=correct_list)
		other_list = List.objects.create()
		Item.objects.create(text='Other Item 1', list=other_list)
		Item.objects.create(text='Other Item 2', list=other_list)

		response = self.client.get(f'/lists/{correct_list.id}/')

		self.assertContains(response, 'Item 1')
		self.assertContains(response, 'Item 2')
		self.assertNotContains(response, 'Other Item 1')
		self.assertNotContains(response, 'Other Item 2')

class NewListTest(TestCase):
	def test_can_save_a_POST_request(self):
		response = self.client.post('/lists/new/', data={'body': 'Buy some eggs.'})

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'Buy some eggs.')

	def test_redirects_after_POST(self):
		response = self.client.post('/lists/new/', data={'body': 'Buy some eggs.'})
		new_list = List.objects.first()

		self.assertRedirects(response, f'/lists/{new_list.id}/')

class NewItemTest(TestCase):
	def test_can_save_a_POST_request_to_an_existing_list(self):
		correct_list = List.objects.create()
		other_list = List.objects.create()

		self.client.post(
			f'/lists/{correct_list.id}/add_item/',
			data={'body': 'New Item'}
		)

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'New Item')
		self.assertEqual(new_item.list, correct_list)

	def test_redirect_to_list_view(self):
		list_ = List.objects.create()
		response = self.client.post(
			f'/lists/{list_.id}/add_item/',
			data={'body': 'New Item'}
		)

		self.assertRedirects(response, f'/lists/{list_.id}/')

	def test_passes_corect_list_in_template(self):
		list_ = List.objects.create()
		response = self.client.get(f'/lists/{list_.id}/')
		self.assertEqual(response.context['list'], list_)