from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'citymap', views.citymap, name='citymap'),
	url(r'cityinformation', views.cityinformation, name='cityinformation'),
]