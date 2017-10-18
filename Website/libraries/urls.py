from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from libraries.models import Library, maps
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=Library.objects.all(),
                                    template_name="libraries/test.html")),
                url(r'^maptest/', ListView.as_view(
                                    queryset= maps.objects.all(),
                                    template_name="libraries/testmap.html")),
  ##              url(r'^colleges/',
                ]

