from django import forms

class comForm(forms.Form):
    this_comment =forms.CharField(label='',widget=forms.Textarea)
