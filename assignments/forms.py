from django import forms

from forum.models import Post
from forum.forms import RTFField

import bleach

import pprint
# pprint.PrettyPrinter().pprint(vars(self))

class NewAssignmentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'anonymous', 'content', 'attachment', 'due_date']
        field_classes = {
                'content': RTFField
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
