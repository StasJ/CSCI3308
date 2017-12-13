from django import forms

from .models import Post

import pprint
# pprint.PrettyPrinter().pprint(vars(self))

class RTFInput(forms.widgets.Input):
    input_type = 'text'
    template_name = 'forum/summernote_widget.html'

    def __init__(self, attrs={'class':'summernote'}, **kwargs):
        print("--------------- RTFInput.__init__ ------------")
        pprint.PrettyPrinter().pprint(attrs)
        if attrs['class'] != 'summernote':
            if attrs['class'] is None:
                attrs['class'] = 'summernote'
            else:
                attrs['class'] += ' summernote'
        super().__init__(attrs, **kwargs)

class RTFField(forms.CharField):
    widget = RTFInput

    def __init__(self, *args, **kwargs):
        if kwargs['widget'] == forms.Textarea:
            # ModelForm > TextField passes in widget=forms.Textarea
            kwargs['widget'] = RTFInput
        super().__init__(*args, **kwargs)


    def clean(self, value):
        return super().clean(value)


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'anonymous', 'content', 'tags']
        field_classes = {
                'content': RTFField
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['content'].widget.attrs.update({'class' : 'materialize-textarea'})


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'anonymous']
        labels = {'content': "Add a reply"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class' : 'materialize-textarea'})
