from django import forms

from .models import Post
# import pprint
# pprint.PrettyPrinter().pprint(vars(self))

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'anonymous', 'content', 'tags']

    def is_valid(self):
        return self.data.get('anonymous', False)
