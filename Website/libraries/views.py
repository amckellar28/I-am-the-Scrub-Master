from django.shortcuts import render

def my_view(request):
    name =  None
    last = None
    if request.user.is_authenticated():
        name = request.user.first_name
        last = request.user.last_name
