from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.utils.html import escape

from lessons.models import Lesson
from lessons.views import home_page

from unittest import skipIf

class HomePageTest(TestCase):
    maxDiff = None

    def test_home_page_uses_correct_template(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertMultiLineEqual(response.content.decode(), expected_html)

    def test_home_page_gets_recent_lessons_first(self):
        Lesson.objects.create(title='Mastoklet', text="Lasterton fidler", published=True)
        Lesson.objects.create(title='Tendamosi', text="Lasterton fidler", published=True)
        request = HttpRequest()
        response = home_page(request)
        oldest_post_index = response.content.index(b'Mastoklet')
        newer_post_index = response.content.index(b'Tendamosi')
        self.assertTrue(newer_post_index < oldest_post_index)

    def test_home_page_only_displays_published(self):
        lastop = Lesson.objects.create(title='Lastop', text="Lopsit Opretanium zesto fastzl")
        tendam = Lesson.objects.create(title='Tendamosi', text="Prewop triconis respoticranium")
        pelo   = Lesson.objects.create(title='Undl Prundwata Pelo', text="Preppatonista lesto", published=True)
        all_lessons = Lesson.objects.all()
        self.assertEquals(len(all_lessons), 3)

        request = HttpRequest()
        response = home_page(request)
        page = str(response.content)

        self.assertTrue(b'Undl Prundwata Pelo' in response.content)
        self.assertTrue(b'Lastop' not in response.content)
        self.assertTrue(b'Tendamosi' not in response.content)