from django.contrib import admin
from .models import Lesson

# Register your models here.
class LessonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lesson, LessonAdmin)
