from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, DetailView

from lessons.models import Lesson

urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
     model=Lesson,
     template_name = 'home.html',
     context_object_name = "lesson", 
     paginate_by=5,
     )),
        # Individual posts
    #url(r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9_]+)/?$', DetailView.as_view(
    #url(r'^(?P<created__year>\d{4})/(?P<created__month>\d{1,2})/(?P<created__day>\d{1,2})/(?P<pk>\d+)/?$', DetailView.as_view(
    url(r'^(?P<created__year>\d{4})/(?P<created__month>\d{1,2})/(?P<created__day>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
    #url(r'^(?P<pkid>\d{1})/?$', DetailView.as_view(
        model=Lesson,
        template_name = 'lesson.html',
        context_object_name = "lesson",
        )),

    #url(r'^$', 'lessons.views.home_page', name='home'),
    url(r'^lessons/', include('lessons.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
