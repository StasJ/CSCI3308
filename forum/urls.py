from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

app_name = 'forum'
urlpatterns = [
    url(r'^$', views.ForumView.as_view(), name='index'),
    # url(r'^test/', views.IndexView.as_view(), name='detail'),
    url(r'^new/', views.NewView.as_view(), name='new'),
    url(r'^(?P<post_id>[0-9]+)/', views.PostView.as_view(), name='detail'),
]
