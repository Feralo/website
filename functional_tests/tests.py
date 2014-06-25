from django.contrib.staticfiles.testing import StaticLiveServerCase
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import sys

import time


class NewProjectTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_define_a_project_and_retreive_it_later(self):
        # Business person visits the website and it returns a webpage
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)
        
        
        # taking a look at the title, the user confirms that this project was
        # written in a real framework
        self.assertIn('Django', self.browser.title)
        time.sleep(2)
        self.fail('finish testing')

if __name__ == '__main__':
    unittest.main(warnings='ignore')