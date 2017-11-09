from django.db import models
from django.conf import settings

from course.models import Course

class Assignment(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    due = models.DateTimeField()
    description = models.TextField()

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
    file = models.FileField(blank=True) # TODO
    content = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    grade = models.IntegerField(blank=True, null=True)
    when = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if (self.content is None     and self.file is None) or \
           (self.content is not None and self.file is not None):
            raise ValidationError('Assignment submission must either be a text submission or a file.')

    def __str__(self):
        return assignment.name + ', ' + user.get_full_name()

