from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'tourist/home.html')
	
def cityinformation(request):
	return render(request, 'tourist/cityinformation.html')
	
def citymap(request):
	return render(request, 'tourist/citymap.html')