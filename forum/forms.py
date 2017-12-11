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

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'anonymous']
        labels = {'content': "Add a reply"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class' : 'materialize-textarea'})
