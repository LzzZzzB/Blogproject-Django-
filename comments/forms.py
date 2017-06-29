'''
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm): #继承自forms.modelform
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
'''



from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']