from django import forms
from .models import Question, Choices
from django.contrib.auth.models import User


class PollForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class QuestionForm(forms.Form):
    question_text = forms.CharField()


class ChoicesForm(forms.Form):
    choice_text = forms.CharField(required=False)
