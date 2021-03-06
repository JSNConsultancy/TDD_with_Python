from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class NewVisitorTest(LiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get(self.live_server_url)
        # She notices the page title and header mention to-do lists
        
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertEqual(
                    inputbox.get_attribute('placeholder'),
                    'Enter a to-do item'
        )

        # she types "Buy peacock feathers" into a text box
        # (Ediths hobby is tying fly fishing lures)
        inputbox.send_keys('Buy peacock feathers')


        # When she hits enter, the page updates and now the page lists
        #"1: Buy peacock feathers" as an item in a todo list
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')


        # There is still a test box inviting her to add another item
        # She enters 'Use Peacock feathers to make fly (Edith is very methodical)'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use Peacock feathers to make fly')
        inputbox.send_keys(Keys.ENTER)

        # The page has updated to reflect both items on the list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use Peacock feathers to make fly')


        # Edith wonders wether the site will remember her list. Thens she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect
        self.fail('Finish writing the test!')
        # She visits that URL - her to-do list is still there.

        # Satisfied she goes to sleep



