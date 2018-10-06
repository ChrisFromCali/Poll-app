from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from poll.forms import PollForm
from .models import Question, Choices
from .forms import ChoicesForm, QuestionForm
from django.forms import formset_factory


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        context = {
            'user': user
        }
        return render(request, 'poll/user-home.html', context)
    else:
        recent_polls = Question.objects.all().order_by('-id')[:10]
        for poll in recent_polls:
            print(poll.question_text)
            for choice in poll.choices_set.all():
                print(choice)
        context = {'polls': recent_polls}
        return render(request, 'poll/home.html', context)


def create(request):
    ChoicesFormSet = formset_factory(ChoicesForm)
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
                print(form)
                if(form):
                    print(form['choice_text'])
                    q.choices_set.create(choice_text=form['choice_text'])
            q.save()
        return redirect('poll-view', q.id)

    else:
        formset = ChoicesFormSet()
        form = {'QuestionForm':QuestionForm, 'formset':formset}
    return render(request, 'poll/create.html', form)

def view(request, poll_id):
    poll = Question.objects.get(id=poll_id)
    context = {
        'poll': poll,
        'poll_id': poll_id
    }
    return render(request, 'poll/view.html', context)

def vote_noid(request):
    return HttpResponse("It worked")

def vote(request, poll_id):
    if request.method == 'POST':
        print(request.POST['choice'])
        choice_selected = Question.objects.get(id=poll_id).choices_set.get(id=request.POST['choice'])
        choice_selected.votes += 1
        choice_selected.save()
        return redirect('poll-results', poll_id)
    else:
        return redirect('poll-view', poll_id)

def results(request, poll_id):
    return HttpResponse("Results for " + str(poll_id))


