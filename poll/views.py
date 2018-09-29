from django.shortcuts import render, HttpResponse, redirect
from poll.forms import PollForm
from .models import Question, Choices
# Create your views here.
def home(request):
    return HttpResponse('<h1>Polls home</h1>')

def create(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            c1 = form.cleaned_data['c1']
            c2 = form.cleaned_data['c2']
            c3 = form.cleaned_data['c3']

    else:
        form = PollForm()
    return render(request, 'poll/create.html', {'form': form})
