from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to-do app. She goes
		# and visits its home page.
		self.browser.get('http://localhost:8000/')

		# She notices the page title and header mentions to-do lists
		self.assertIn('To-Do', self.browser.title)

		self.fail('Finish the tests!')

		# She is invited to enter a to-do item right away

		# She types "Buy peacock feathers" into a textbox

		# When she hits enter, the page updates, and now the page lists
		# "1. Buy peacock feathers"

		# There is still a box inviting her to add another item. She enters
		# "Use peacock feathers to make a fly"

		# The page updates again, and now both items are on the list

		# Edith wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect

		# She visits that URL - her to-do list is still there

		# Satisfied, she goes back to sleep


if __name__ == '__main__':
	unittest.main()