from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from taggit.managers import TaggableManager

from course.models import Course

# TODO
# https://github.com/alex/django-taggit
# https://github.com/shanbay/django-vote

def attachment_path(post, filename):
    return 'post_{0}/{1}'.format(post.id, filename)

class Post(models.Model):
    FORUM = 1
    COMMENT = 2
    ASSIGNMENT = 3
    SUBMISSION = 4
    TYPE_CHOICES = (
            (FORUM, 'Forum Post'),
            (FORUM, 'Comment'),
            (ASSIGNMENT, 'Assignment'),
            (SUBMISSION, 'Assignment Submission')
    )

    title = models.CharField(max_length=64)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    anonymous = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)
    content = models.TextField(blank=True)
    tags = TaggableManager(blank=True)
    pub_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)


    attachment = models.FileField(blank=True, null=True, upload_to=attachment_path);
    type = models.IntegerField(choices=TYPE_CHOICES, default=FORUM)
    due_date = models.DateTimeField(null=True)
    grade = models.IntegerField(blank=True, null=True)


    def clean_fields(self, exclude=None):
        super(Post, self).clean_fields(exclude=exclude)
        if self.parent == self:
            raise ValidationError({'parent': 'Parent cannot be self.'})

    def author_name(self):
        if self.anonymous:
            return "Anonymous"
        else:
            return self.user.get_full_name()

    def get_grade_string(self, user_id):
        try:
            lastGraded = self.post_set.filter(user_id=user_id, grade__isnull=False).latest(field_name='pub_time')
            return lastGraded.grade
        except ObjectDoesNotExist:
            return '-'

    def __str__(self):
        return self.title
