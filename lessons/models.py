from django.db import models

# Create your models here.

class Lesson(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(default='')
