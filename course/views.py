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
        context['course_list'] = self.request.user.course_set.all()

        context['info_shown'] = self.request.session.get('info_shown', default=False)
        self.request.session['info_shown'] = True

        return context

    def test_func(self):
        return self.request.user.course_set.filter(id=self.kwargs['course_id']).exists()

def courseHomeRedirect(request, course_id=None):
    if course_id is None:
        course_id = 1
    return HttpResponseRedirect(reverse('forum:index', args=[course_id]))
