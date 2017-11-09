from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone

from course.models import Course

class Assignment(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    publish_time = models.DateTimeField(default=timezone.now)
    grades_published = models.BooleanField(default=False)
    due = models.DateTimeField()
    description = models.TextField()
    accept_late = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AssignmentAttachment(models.Model):
    name = models.CharField(max_length=64)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    file = models.FileField() # TODO

    def __str__(self):
        return self.name


class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(blank=True, null=True) # TODO
    content = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    grade = models.IntegerField(blank=True, null=True)
    when = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if (self.content and self.file) or \
           (not self.content and not self.file):
            raise ValidationError('Assignment submission must either be a text submission or a file.')
        if (not self.assignment.accept_late and self.assignment.due < timezone.now()):
            raise ValidationError('Assignment is pass due and does not accept late submissions.')

    def __str__(self):
        return self.assignment.course.get_name() + ': ' + self.assignment.name + ': ' + self.user.get_full_name()


