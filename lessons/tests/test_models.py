from django.test import TestCase
from django.core.exceptions import ValidationError
import datetime
from lessons.models import Lesson

class LessonModelsTest(TestCase):
    #fixtures = ['lessons.json'] # 2 fixtures here, let's add 2 more

    def test_saving_and_retreiving_lessons(self):
        first_lesson = Lesson()
        first_lesson.title = "Title of first lesson"
        first_lesson.text = "Text of first lesson"
        first_lesson.save()
        first_lesson.full_clean()

        second_lesson = Lesson()
        second_lesson.title = "Titulo de la segunda lesson"
        second_lesson.text = "Texto de la segunda"
        second_lesson.save()
        second_lesson.full_clean()

        saved_lessons = Lesson.objects.all()
        self.assertEqual(saved_lessons.count(), 2)

        recent_saved_lesson = saved_lessons[0]
        oldest_saved_lesson = saved_lessons[1]

        self.assertEqual(oldest_saved_lesson.title, first_lesson.title)
        self.assertEqual(oldest_saved_lesson.text, first_lesson.text)

        self.assertEqual(recent_saved_lesson.title, second_lesson.title)
        self.assertEqual(recent_saved_lesson.text, second_lesson.text)


    def test_cannot_save_empty_lesson(self):
        lesson = Lesson(title="listo", text='')
        with self.assertRaises(ValidationError):
            lesson.save()
            lesson.full_clean()

    def test_lesson_default_ordering(self):
        lesson1 = Lesson.objects.create(title='title 1', text='i1')
        lesson2 = Lesson.objects.create(title='title 2', text='item 2')
        lesson3 = Lesson.objects.create(title='title 3', text='3')
        self.assertEqual(
            list(Lesson.objects.all()),
            [lesson3, lesson2, lesson1]
        )

    def test_string_representation(self):
        item = Lesson(title="Fancy babies",text='some text to represent in a view (not a title)')
        self.assertEqual(str(item), "Fancy babies")