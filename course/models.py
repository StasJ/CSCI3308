from django.db import models
from django.conf import settings

from alma.models import School

class Course(models.Model):
    department = models.CharField(max_length=4)
    number = models.IntegerField()
    title = models.CharField(max_length=64)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    pin = models.CharField(max_length=16, blank=True, null=True)

    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership')

    def __str__(self):
        return self.department + ' ' + str(self.number) + ': ' + self.title;

    def get_name(self):
        return self.department + ' ' + str(self.number)

class Membership(models.Model):
    STUDENT = 1
    TA = 2
    PROFESSOR = 3
    TYPE_CHOICES = (
            (STUDENT, 'Student'),
            (TA, 'Teaching Assistant'),
            (PROFESSOR, 'Professor')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,                 on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE_CHOICES, default=STUDENT)

    def __str__(self):
        return str(self.course) + ' ' + str(self.user) + ': ' + self.get_type_display()

# class CourseResource(models.Model):

