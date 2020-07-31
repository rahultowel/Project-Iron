from django import forms

class comForm(forms.Form):
    this_comment =forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Say something about this poll?'}))

class addAnother(forms.Form):
    new_choice =forms.CharField(label='Enter new choice below')
