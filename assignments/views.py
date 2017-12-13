from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from course.views import CourseView
from course.models import Course, Membership
from django.views.generic import TemplateView, FormView, UpdateView
from django.http import Http404


from forum.models import Post
from .forms import NewAssignmentForm, NewSubmissionForm


class AssignmentListView(CourseView):
    template_name = 'assignments/assignment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_prof = self.request.user.membership_set.filter(id=self.kwargs['course_id'], type__gte=Membership.TA).exists()

        context['is_prof'] = is_prof
        context['post_list'] = context['course'].post_set.filter(parent__isnull=True, type=Post.ASSIGNMENT).order_by('-pub_time')
        return context

class AssignmentView(CourseView):
    template_name = 'assignments/detail.html'

    def get_context_data(self, post_id, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=post_id, type=Post.ASSIGNMENT)

        is_prof = self.request.user.membership_set.filter(id=self.kwargs['course_id'], type__gte=Membership.TA).exists()

        context['is_prof'] = is_prof
        context['post'] = post
        if is_prof:
            context['submissions'] = post.post_set.filter(type=Post.SUBMISSION);
        else:
            context['submissions'] = post.post_set.filter(user_id=self.request.user.id, type=Post.SUBMISSION);
        return context

class AssignmentSubmissionView(CourseView, UpdateView):
    template_name = 'assignments/submission_detail.html'
    model = Post
    fields = ['grade']
    object = None
    success_url = None

    def get_context_data(self, post_id, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        assignment = get_object_or_404(Post, pk=post_id, type=Post.ASSIGNMENT)
        submission = get_object_or_404(Post, pk=pk, type=Post.SUBMISSION)

        self.object = submission

        context['assignment'] = assignment
        context['post'] = submission
        return context

    def get_success_url(self):
        return reverse('assignments:detail', args=(self.kwargs['course_id'], self.kwargs['post_id']))



class NewAssignmentView(CourseView, FormView):
    template_name = 'assignments/new_assignment.html'
    form_class = NewAssignmentForm

    def get_form(self):
        if self.request.GET and self.request.GET['id']:
            post = get_object_or_404(Post, pk=self.request.GET['id'], type=Post.ASSIGNMENT)
            return self.form_class(instance=post, **self.get_form_kwargs())
        else:
            return self.form_class(**self.get_form_kwargs())

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

        post.save()

        self.success_url = reverse('assignments:detail', args=(kwargs['course_id'], post.id))
        # self.success_url = self.request.path
        return super().form_valid(form)

class AssignmentSubmitView(CourseView, FormView):
    template_name = 'assignments/new_submission.html'
    form_class = NewSubmissionForm

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
        post.parent_id = kwargs['post_id']
        post.type = Post.SUBMISSION
        post.title = "Submission for Assignment " + kwargs['post_id']

        post.save()

        self.success_url = reverse('assignments:detail', args=(kwargs['course_id'], kwargs['post_id']))
        return super().form_valid(form)
