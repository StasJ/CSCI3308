from django.db import models
from django.conf import settings

from course.models import Course

# TODO
# https://github.com/alex/django-taggit
# https://github.com/shanbay/django-vote

class Post(models.Model):
    title = models.CharField(max_length=64)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    anonymous = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)
    content = models.TextField()

    def __str__(self):
        return self.title
