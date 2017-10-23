from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'businessman/home.html')
	
def cityinformation(request):
	return render(request, 'businessman/cityinformation.html')
	
def citymap(request):
	return render(request, 'businessman/citymap.html')