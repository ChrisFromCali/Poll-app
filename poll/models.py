from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=128)
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.question_text

class Choices(models.Model):
    choice_text = models.CharField(max_length=256)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

""" class ChoicesForm(ModelForm):
class Meta:
    model = Choices
    fields = ['choice_text'] """