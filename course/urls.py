from django.conf.urls import url, include
from django.views.generic import TemplateView

# app_name = 'course'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='course/index.html'), name='course_index'),
    url(r'^(?P<course_id>[0-9]+)/$', TemplateView.as_view(template_name='course/index.html'), name='course_index'),
    url(r'^(?P<course_id>[0-9]+)/', include([
        url(r'^forum/', include('forum.urls')),
    ])),
]
