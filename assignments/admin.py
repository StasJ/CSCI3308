from django.contrib import admin

from .models import Assignment, AssignmentAttachment, AssignmentSubmission

admin.site.register(Assignment)
admin.site.register(AssignmentAttachment)
admin.site.register(AssignmentSubmission)
