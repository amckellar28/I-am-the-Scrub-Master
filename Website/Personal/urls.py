from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^home$', views.index, name='index'),
	url(r'^$', views.selectcity, name='selectcity'),
    url(r'^advising/denied', views.accessdenied, name='accessdenied'),
]