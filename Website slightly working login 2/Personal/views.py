from django.shortcuts import render

# Create your views here.
def selectcity(request):
	return render(request, 'Personal/selectcity.html')

def index(request):
	return render(request, 'Personal/home.html')