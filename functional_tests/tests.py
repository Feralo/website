from django.contrib.staticfiles.testing import StaticLiveServerCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

import time


class NewLessonTest(StaticLiveServerCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_home_page_lists_lessons(self):
        # a person visits the website and it returns a webpage
        self.browser.get(self.server_url)
        self.browser.implicitly_wait(3)
        
        
        # taking a look at the title, the user confirms that this project was
        # written in a 'real' framework
        self.assertIn('Django', self.browser.title)
        #time.sleep(1)
          
        # looking at the page that loaded, visitor sees lessons area
        lessons_container = self.browser.find_element_by_id('lessons')
        
        # the title of most recent lesson posted at the top of the area

            # How should I test for this test fixtures??
        
        # the next older lesson is listed after that
        
        # each lesson lists the author 
           
        # and publication date
        
        # He is allowed to enter a to-do item right away
        
        #self.fail('finish testing')

if __name__ == '__main__':
    unittest.main(warnings='ignore')