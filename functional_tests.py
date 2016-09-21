from selenium import webdriver
import unittest




class NewVisitorTest(unittest.TestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        """ Edith has heard about a cool new online to-do app.
        She goes to check out its homepage"""

        # She notices the page title and header mention to-do lists
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        # she types "Buy peacock feathers" into a text box
        # (Ediths hobby is tying fly fishing lures)

        # When she hits enter, the page updates and now the page lists
        #"1: Buy peacock deathers" as an item in a todo list

        # There is still a test box inviting her to add another item
        # She enters 'Use Peacock feathers to make fly (Edith is very methodical)'

        # The page has updated to reflect both items on the list

        # Edith wonders wether the site will remember her list. Thens she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect

        # She visits that URL - her to-do list is still there.

        # Satisfied she goes to sleep





if __name__=='__main__':
    unittest.main(warnings='ignore')


