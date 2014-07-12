from django.test import TestCase
from django.core.exceptions import ValidationError

from lessons.models import Lesson

class LessonModelsTest(TestCase):

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

        first_saved_lesson = saved_lessons[0]
        second_saved_lesson = saved_lessons[1]

        self.assertEqual(first_saved_lesson.title, "Title of first lesson")
        self.assertEqual(first_saved_lesson.text, "Text of first lesson")

        self.assertEqual(second_saved_lesson.title, "Titulo de la segunda lesson")
        self.assertEqual(second_saved_lesson.text, "Texto de la segunda")


    def test_cannot_save_empty_lesson(self):
        lesson = Lesson(title="listo", text='')
        with self.assertRaises(ValidationError):
            lesson.save()
            lesson.full_clean()