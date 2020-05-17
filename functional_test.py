from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_table(self, text, table_id):
		table = self.browser.find_element_by_id(table_id)
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to-do app. She goes
		# and visits its home page.
		self.browser.get('http://localhost:8000/')

		# She notices the page title and header mentions to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item right away
		inputbox = self.browser.find_element_by_id('new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# She types "Buy peacock feathers" into a textbox
		inputbox.send_keys('Buy peacock feathers')

		# When she hits enter, the page updates, and now the page lists
		# "1. Buy peacock feathers"
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		self.check_for_row_in_table('1. Buy peacock feathers', 'todo_table')

		# There is still a box inviting her to add another item. She enters
		# "Use peacock feathers to make a fly"
		inputbox = self.browser.find_element_by_id('new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		# The page updates again, and now both items are on the list
		self.check_for_row_in_table('1. Buy peacock feathers', 'todo_table')
		self.check_for_row_in_table('2. Use peacock feathers to make a fly', 'todo_table')

		self.fail('Finish the test!')

		# Edith wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect

		# She visits that URL - her to-do list is still there

		# Satisfied, she goes back to sleep


if __name__ == '__main__':
	unittest.main()