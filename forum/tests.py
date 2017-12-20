from django.test import TestCase

from .models import Post

class PostModelTests(TestCase):
    def test_get_anonymous_name(self):
        post = Post(user_id=1, anonymous=True)
        self.assertEqual(post.author_name(), "Anonymous")
