from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def student_group(user):
    return user.is_authenticated() and user.groups.filter(name='Student').exists()

@login_required
@user_passes_test(student_group, login_url='/advising/denied/')
def my_view(request):
    return render(request, 'libraries/test.html')
