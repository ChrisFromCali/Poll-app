from django.shortcuts import render, HttpResponse, redirect
from poll.forms import PollForm
from .models import Question, Choices, QuestionForm, ChoicesForm
from django.forms import formset_factory


# Create your views here.
def home(request):
    return HttpResponse('<h1>Polls home</h1>')

def create(request):
    ChoicesFormSet = formset_factory(ChoicesForm)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, prefix='question')
        choices_formset = ChoicesFormSet(request.POST, prefix='choices')
        
        
        formset = ChoicesFormSet()
        for form in formset:
            print(form.as_table())

        return redirect('poll-create')

    else:
        choices_formset = ChoicesFormSet()
        form = {'QuestionForm':QuestionForm(prefix='question'), 'ChoicesFormSet':choices_formset}
    return render(request, 'poll/create.html', form)
