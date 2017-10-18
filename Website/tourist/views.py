from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def tourist_group(user):
    return user.is_authenticated() and user.groups.filter(name='Tourist').exists()

@login_required
@user_passes_test(tourist_group, login_url='/advising/denied/')
def index(request):
	return render(request, 'tourist/home.html')

@login_required
@user_passes_test(tourist_group, login_url='/advising/denied/')
def cityinformation(request):
	return render(request, 'tourist/cityinformation.html')

@login_required
@user_passes_test(tourist_group, login_url='/advising/denied/')
def citymap(request):
	return render(request, 'tourist/citymap.html')