from django.db import models
from django.conf import settings

from alma.models import School

class Course(models.Model):
    name = models.CharField(max_length=64)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

