from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lessons.views.home_page', name='home'),
    url(r'^lessons/', include('lessons.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
