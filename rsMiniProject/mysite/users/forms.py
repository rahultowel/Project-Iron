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
    description=forms.CharField(label='Description',widget=forms.Textarea(), required=False)
    choice1=forms.CharField(label='Choice 1',max_length=200)
    choice2=forms.CharField(label='Choice 2', max_length=200)

class givePerm(forms.Form):
    perm= forms.IntegerField(label='I understand that by clicking "approve", the choice will be added to my question and clicking "deny" will permanently delete the request.',
    widget=forms.HiddenInput(),initial=0)
