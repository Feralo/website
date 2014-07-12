from django.shortcuts import render
from lessons.models import Lesson

def home_page(request):
    lessons = Lesson.objects.all()
    return render(request, 'home.html', {'lesson':lessons})
