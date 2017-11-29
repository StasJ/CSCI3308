from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from course.models import Course

class CourseView(TemplateView):
    template_name = 'course/index.html'

    def get_context_data(self, course_id, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        course = get_object_or_404(Course, pk=course_id)
        context['course'] = course
        context['course_list'] = Course.objects.all()
        return context
