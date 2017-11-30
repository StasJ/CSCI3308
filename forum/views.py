from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic import TemplateView, FormView
from django.urls import reverse

from course.views import CourseView
from course.models import Course

from .models import Post
from .forms import NewPostForm

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

class NewView(CourseView, FormView):
    template_name = 'forum/new.html'
    form_class = NewPostForm

    def get_context_data(self, **kwargs):
        kwargs = self.kwargs # post -> form_invalid does not pass in kwargs
        context = super(NewView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        kwargs = self.kwargs # post does not pass in kwargs
        # save new post here
        self.success_url = reverse('forum:detail', args=(kwargs['course_id'], 1))
        return super(NewView, self).form_valid(form)

