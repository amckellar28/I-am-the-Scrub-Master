from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def businessman_group(user):
    return user.is_authenticated() and user.groups.filter(name='Businessman').exists() or admin_group(user)

def admin_group(user):
    return user.is_authenticated() and user.is_staff

  
@login_required
@user_passes_test(businessman_group, login_url='/advising/denied/')
def index(request):
	return render(request, 'businessman/home.html')

@login_required	
@user_passes_test(businessman_group, login_url='/advising/denied/')
def cityinformation(request):
	return render(request, 'businessman/cityinformation.html')

@login_required
@user_passes_test(businessman_group, login_url='/advising/denied/')
def citymap(request):
	return render(request, 'businessman/citymap.html')