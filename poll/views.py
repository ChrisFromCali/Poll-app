from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from poll.forms import PollForm
from .models import Question, Choices
from .forms import ChoicesForm, QuestionForm
from django.forms import formset_factory


# Create your views here.
def home(request):
    return HttpResponse('<h1>Polls home</h1>')

def create(request):
    ChoicesFormSet = formset_factory(ChoicesForm, extra=3)
    if request.method == 'POST':
        questionForm = QuestionForm(request.POST)
        
        formset = ChoicesFormSet(request.POST)

        if ((questionForm.is_valid()) and (formset.is_valid())):
            if request.user.is_authenticated:
                username = request.user.username
                user = User.objects.filter(username=username).first()
                q = Question(question_text=questionForm.cleaned_data['question_text'], author=user)
            else:
                q = Question(question_text=questionForm.cleaned_data['question_text'])
            
            q.save()
            for form in formset.cleaned_data:
                print(form['choice_text'])
                q.choices_set.create(choice_text=form['choice_text'])
            q.save()
        return redirect('poll-create')

    else:
        formset = ChoicesFormSet()
        form = {'QuestionForm':QuestionForm, 'formset':formset}
    return render(request, 'poll/create.html', form)
