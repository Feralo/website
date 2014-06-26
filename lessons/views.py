from django.shortcuts import render
from lessons.models import Lesson

# Create your views here.
def home_page(request):
    lessons = Lesson.objects.all()
    return render(request, 'home.html', {'lesson':lessons})
