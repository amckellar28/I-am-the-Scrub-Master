from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from libraries.models import Library

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=Library.objects.all(),
                                    template_name="libraries/test.html")),
                ]
