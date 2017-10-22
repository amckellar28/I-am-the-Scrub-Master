from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'student/home.html')
	
def cityinformation(request):
	return render(request, 'student/cityinformation.html')
	
def citymap(request):
	return render(request, 'student/citymap.html')