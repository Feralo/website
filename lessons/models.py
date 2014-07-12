from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(default='')
