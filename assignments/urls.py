from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

app_name = 'assignments'
urlpatterns = [
    url(r'^$', views.AssignmentListView.as_view(), name='index'),
    url(r'^new/', views.NewAssignmentView.as_view(), name='new'),
    url(r'^(?P<post_id>[0-9]+)/submition/(?P<pk>[0-9]+)', views.AssignmentSubmissionView.as_view(), name='submission'),
    url(r'^(?P<post_id>[0-9]+)/submit', views.AssignmentSubmitView.as_view(), name='submit'),
    url(r'^(?P<post_id>[0-9]+)/', views.AssignmentView.as_view(), name='detail'),
]
