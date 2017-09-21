from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
	 
def student_group(user):
    return user.is_authenticated() and user.groups.filter(name='Student').exists()

def tourist_group(user):
    return user.is_authenticated() and user.groups.filter(name='Tourist').exists()

def enter_view(request):
    if request.user.groups.filter(name='Student'):
        return redirect('/student/')
    elif request.user.groups.filter(name='Businessman'):
        return redirect('/businessman/')
    elif request.user.groups.filter(name='Tourist'):
        return redirect('/tourist/')
    else:
        return redirect('/advising/denied/')

@login_required (login_url="login/")
@user_passes_test(student_group, login_url='/advising/denied/')
def index(request):
	return render(request, 'student/home.html')

@login_required	(login_url="login/")
@user_passes_test(student_group, login_url='/advising/denied/')
def cityinformation(request):
	return render(request, 'student/cityinformation.html')

@login_required (login_url="login/")
@user_passes_test(student_group, login_url='/advising/denied/')
def citymap(request):
	return render(request, 'student/citymap.html')