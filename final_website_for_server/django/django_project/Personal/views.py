from django.shortcuts import render

# Create your views here.
def selectcity(request):
	return render(request, 'Personal/selectcity.html')

##def index(request):
##	return render(request, 'Personal/home.html')
    
def accessdenied(request):
	return render(request, 'Personal/accessdenied.html')
    
def contactus(request):
    return render(request, 'Personal/contactus.html')
    
def FAQ(request):
    return render(request, 'Personal/FAQ.html')