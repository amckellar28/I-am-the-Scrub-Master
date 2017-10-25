from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signupstudent/$', views.signup, name='signup'),
    url(r'^signupbusiness/$', views.signupbusiness, name='signup'),
    url(r'^signuptourist/$', views.signuptourist, name='signup')
    ]
