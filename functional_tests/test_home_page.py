from django.contrib.staticfiles.testing import StaticLiveServerCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
import sys

import time


class HomePageTest(FunctionalTest):
    fixtures = ['lessons.json']

    def test_home_page_lists_lessons(self):
        # a person visits the website and it returns a webpage
        self.browser.get(self.server_url)
        self.browser.implicitly_wait(3)


        # taking a look at the title, the user confirms that this project was
        # written in a 'real' framework
        self.assertIn('feralo', self.browser.title)

        # looking at the page that loaded, visitor sees lessons area
        lessons_container = self.browser.find_element_by_id('lessons')

        # lesson has a title
        self.browser.find_element_by_css_selector(".blog-post")

        # and publication date
        pub_date = self.browser.find_element_by_css_selector(".blog-post-meta").text

        # test that this is a date 

        # the title of most recent lesson posted first

        # the next older lesson is listed after that

        #self.fail('finish testing')

if __name__ == '__main__':
    unittest.main(warnings='ignore')