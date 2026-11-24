from django.forms import ModelForm
from .models import *


class RequestFrom(ModelForm):
    class Meta:
        model = Request
        fields = ['user', 'comment']

class CommentFrom(ModelForm):
    class Meta:
        model = Comment
        fields = ['request', 'text']
