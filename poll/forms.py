from django import forms
from .models import Question, Choices
from django.contrib.auth.models import User


class PollForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        