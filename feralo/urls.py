from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView

from lessons.models import Lesson

urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
     model=Lesson,
     template_name = 'home.html',
     context_object_name = "lesson", 
     paginate_by=5,
     )),
    #url(r'^$', 'lessons.views.home_page', name='home'),
    url(r'^lessons/', include('lessons.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
