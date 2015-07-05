from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.utils.html import escape
from django.utils import timezone

from lessons.models import Lesson
from lessons.views import home_page

from unittest import skipIf
import markdown

class HomePageTest(TestCase):
    fixtures = ['lessons.json']
    maxDiff = None

    def test_home_page_uses_correct_template(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertMultiLineEqual(response.content.decode(), expected_html)

    def test_home_page_gets_recent_lessons_first(self):
        response = self.client.get('/')

        older_post_index = response.content.index(b'Prundwata')
        newer_post_index = response.content.index(b'Financial')
        self.assertTrue(newer_post_index > older_post_index)

    #@skipIf(True,"not yet implemented")
    def test_view_displays_markdown(self):
        expected_html_from_markdown_fixture="<img alt=\"scatter\" src=\"http://i.imgur.com/BsNgZaQl.png\""
        response = self.client.get('/')
        self.assertTrue(expected_html_from_markdown_fixture in str(response.content))

    def test_home_page_only_displays_published(self):
        all_lessons = Lesson.objects.all()
        self.assertEquals(len(all_lessons), 3)

        response = self.client.get('/')

        self.assertTrue(b'Undl Prundwata Pelo' in response.content)
        self.assertTrue(b'Lastop' not in response.content)
        self.assertTrue(b'Tendamosi' not in response.content)
