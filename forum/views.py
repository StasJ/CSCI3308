from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic import TemplateView

from .models import Post
from course.models import Course

class ForumView(TemplateView):
    template_name = 'forum/index.html'

    def get_context_data(self, course_id, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        course = get_object_or_404(Course, pk=course_id)
        context['course'] = course
        context['post_list'] = course.post_set.exclude(parent__isnull=False).order_by('-pub_time')
        context['course_list'] = Course.objects.all()
        return context

class PostView(TemplateView):
    template_name = 'forum/detail.html'

    def get_context_data(self, course_id, post_id, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        course = get_object_or_404(Course, pk=course_id)
        post   = get_object_or_404(Post,   pk=post_id)
        context['course'] = course
        context['post'] = post
        context['course_list'] = Course.objects.all()
        return context

class NewView(TemplateView):
    template_name = 'forum/new.html'

    def get_context_data(self, course_id, **kwargs):
        context = super(NewView, self).get_context_data(**kwargs)
        course = get_object_or_404(Course, pk=course_id)
        context['course'] = course
        return context
