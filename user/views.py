from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserSearchForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You can now login')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form':form})

def user_search(request):
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('user', form.cleaned_data['username'])
    else:
        form = UserSearchForm()
        return render(request, 'user/user_search.html', {'form':form})

def user(request, username):
    user = User.objects.get(username=username)
    return render(request, 'poll/user-home.html', {'user':user})

