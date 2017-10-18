from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from . forms import SignUpForm
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

def index(request):
    return render(request, 'registration/home2.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            g1 = Group.objects.get(name='Student')
            g1.user_set.add(user)
            login(request, user)
            return redirect('/library')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def signupbusiness(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            g1 = Group.objects.get(name='Businessman')
            g1.user_set.add(user)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def signuptourist(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            g1 = Group.objects.get(name='Tourist')
            g1.user_set.add(user)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

