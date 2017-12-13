from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic import TemplateView, FormView
from django.urls import reverse
from django.contrib.auth import get_user

from course.views import CourseView
from course.models import Course

from .models import Post
from .forms import NewPostForm, NewCommentForm

class ForumView(CourseView):
    template_name = 'forum/posts.html'

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['post_list'] = context['course'].post_set.exclude(parent__isnull=False).order_by('-pub_time')
        return context


class PostView(CourseView, FormView):
    # template_name = 'forum/detail_metro.html'
    template_name = 'forum/detail.html'
    form_class = NewCommentForm

    def get_context_data(self, post_id, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=post_id)
        context['post'] = post
        return context

    def form_valid(self, form):
        kwargs = self.kwargs # post does not pass in kwargs
        comment = form.save(commit=False)
        comment.user = get_user(self.request)
        comment.course_id = kwargs['course_id']
        comment.parent_id = kwargs['post_id']
        comment.title = "Reply to post " + str(comment.parent_id)
        comment.save()
        self.success_url = reverse('forum:detail', args=(kwargs['course_id'], kwargs['post_id']))
        return super().form_valid(form)


class NewPostView(CourseView, FormView):
    template_name = 'forum/new_post.html'
    form_class = NewPostForm

    def get_context_data(self, **kwargs):
        kwargs = self.kwargs # post -> form_invalid does not pass in kwargs
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        kwargs = self.kwargs # post does not pass in kwargs
        # save new post here
        post = form.save(commit=False)
        post.user = get_user(self.request)
        post.course_id = kwargs['course_id']
        post.save()
        self.success_url = reverse('forum:detail', args=(kwargs['course_id'], post.id))
        return super().form_valid(form)

