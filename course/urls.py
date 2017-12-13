from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

# app_name = 'course'
urlpatterns = [
    url(r'^$', views.courseHomeRedirect, name='course_index'),
    url(r'^(?P<course_id>[0-9]+)/$', views.courseHomeRedirect, name='course_index'),
    url(r'^(?P<course_id>[0-9]+)/', include([
        url(r'^forum/', include('forum.urls')),
        url(r'^assignments/', include('assignments.urls')),
    ])),
]
