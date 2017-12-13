from django.shortcuts import render
from django.views.generic import FormView
from django.conf import settings
from django.urls import reverse

from .forms import RegisterForm
from course.models import Course, Membership

# settings.AUTH_USER_MODEL 

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = '/course/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        for course_id in form.cleaned_data['courses']:
            Membership(user=user, course_id=int(course_id)).save()

        self.success_url = reverse('course_index')
        return super().form_valid(form)
