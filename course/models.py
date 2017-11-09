from django.db import models
from django.conf import settings

from alma.models import School

class Course(models.Model):
    department = models.CharField(max_length=4)
    number = models.IntegerField()
    title = models.CharField(max_length=64)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.department + ' ' + self.number + ': ' + self.title;

# class CourseResource(models.Model):

