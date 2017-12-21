from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.response import TemplateResponse

from .models import Post
from alma.models import User, School
from course.models import Course, Membership

class PostModelTests(TestCase):
    def test_get_anonymous_name(self):
        post = Post(user_id=1, anonymous=True)
        self.assertEqual(post.author_name(), "Anonymous")

    def test_can_user_edit(self):
        user1 = User.objects.create(email="user1@a.com")
        user2 = User.objects.create(email="user2@a.com")
        school = School.objects.create()
        course = Course.objects.create(number=0, school=school)
        membership = Membership.objects.create(user = user1, course=course)
        membership = Membership.objects.create(user = user2, course=course)
        post = Post.objects.create(user = user1, course=course)

        url = reverse('forum:new', args=[course.id]) + "?id={0}".format(post.id)

        self.client.force_login(user1)
        response = self.client.get(url)
        self.assertNotEqual(type(response), HttpResponseNotFound)

        self.client.force_login(user2)
        response = self.client.get(url)
        self.assertEqual(type(response), HttpResponseNotFound)

    def test_can_user_view(self):
        user1 = User.objects.create(email="user1@a.com")
        user2 = User.objects.create(email="user2@a.com")
        school = School.objects.create()
        course = Course.objects.create(number=0, school=school)
        membership = Membership.objects.create(user = user1, course=course)
        # user2 does not have membership in course
        post = Post.objects.create(user = user1, course=course)

        url = reverse('forum:detail', args=[course.id, post.id])

        self.client.force_login(user1)
        response = self.client.get(url)
        self.assertEqual(type(response), TemplateResponse)

        self.client.force_login(user2)
        response = self.client.get(url)
        self.assertEqual(type(response), HttpResponseRedirect)
