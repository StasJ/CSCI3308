from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from course.models import Course

class CourseView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'course/index.html'

    def get_context_data(self, course_id, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        course = get_object_or_404(Course, pk=course_id)
        context['course'] = course
        context['course_list'] = Course.objects.all()
        return context

    def test_func(self):
        return self.request.user.course_set.filter(id=self.kwargs['course_id']).exists()

def courseHomeRedirect(request):
    return HttpResponseRedirect(reverse('course_index', args=[1]))
