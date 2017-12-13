from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from course.views import CourseView
from course.models import Course, Membership
from django.views.generic import TemplateView, FormView


from forum.models import Post
from .forms import NewAssignmentForm


class AssignmentListView(CourseView):
    template_name = 'assignments/assignment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = context['course'].post_set.exclude(parent__isnull=False).order_by('-pub_time')
        return context

class AssignmentView(CourseView):
    template_name = 'assignments/detail.html'

    def get_context_data(self, post_id, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=post_id)
        context['post'] = post
        return context

class NewAssignmentView(CourseView, FormView):
    template_name = 'assignments/new_assignment.html'
    form_class = NewAssignmentForm

    def get_context_data(self, **kwargs):
        kwargs = self.kwargs # post -> form_invalid does not pass in kwargs
        context = super().get_context_data(**kwargs)
        return context

    def test_func(self):
        return super().test_func() and self.request.user.membership_set.filter(id=self.kwargs['course_id'], type__gte=Membership.TA).exists()

    def form_valid(self, form):
        kwargs = self.kwargs # post does not pass in kwargs

        post = form.save(commit=False)
        post.user_id = self.request.user.id
        post.course_id = kwargs['course_id']
        post.type = Post.ASSIGNMENT

        print(vars(post.attachment))

        post.save()

        self.success_url = reverse('assignments:detail', args=(kwargs['course_id'], post.id))
        # self.success_url = self.request.path
        return super().form_valid(form)

