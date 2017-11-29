from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic import TemplateView

from course.views import CourseView
from .models import Post
from course.models import Course

class ForumView(CourseView):
    template_name = 'forum/index.html'

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['post_list'] = context['course'].post_set.exclude(parent__isnull=False).order_by('-pub_time')
        return context

class PostView(CourseView):
    template_name = 'forum/detail.html'

    def get_context_data(self, post_id, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=post_id)
        context['post'] = post
        return context

class NewView(CourseView):
    template_name = 'forum/new.html'

    def get_context_data(self, **kwargs):
        context = super(NewView, self).get_context_data(**kwargs)
        return context
