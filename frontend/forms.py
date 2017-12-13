from django import forms
from django.contrib.auth.forms import UserCreationForm
from alma.models import User
from course.models import Course

class RegisterForm(UserCreationForm):
    courses = forms.MultipleChoiceField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'school']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        courses = Course.objects.all()
        self.fields['courses'].choices = [(c.id, c.get_name()) for c in courses]

# class SignUpForm(forms.ModelForm):
#     # username = forms.EmailField()
#     class Meta:
#         model=User
#         fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

