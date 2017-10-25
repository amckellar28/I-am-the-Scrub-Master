from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from Personal.models import Event


urlpatterns = [
##	url(r'^home$', views.index, name='index'),
	url(r'^$', views.selectcity, name='selectcity'),
    url(r'^contactus', views.contactus, name='contactus'),
    url(r'^faq', views.FAQ, name='FAQ'),
    url(r'^advising/denied', views.accessdenied, name='accessdenied'),
        url(r'^home$', ListView.as_view(
                                    queryset=Event.objects.all(),
                                    template_name="Personal/home.html")),
]
