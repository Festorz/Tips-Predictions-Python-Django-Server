from django import forms
from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    website = forms.CharField(required=False)
    comment = forms.CharField(required=False)
