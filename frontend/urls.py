from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

app_name = 'frontend'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='frontend/index.html'), name='index'),
    url(r'^register/', views.RegisterView.as_view(), name='register'),
]
