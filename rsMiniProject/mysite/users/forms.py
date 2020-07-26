from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    spirit_animal= forms.CharField()

    class Meta:
        model=User
        fields=['username','password1','password2','spirit_animal']

class newQuestionForm(forms.Form):
    question_text=forms.CharField(label='New Question', max_length=200)
    choice1=forms.CharField(label='Choice 1',max_length=200)
    choice2=forms.CharField(label='Choice 2', max_length=200)
