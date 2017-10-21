from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from libraries.models import Library, maps, Zoos, Museums, Colleges, Malls
from libraries.models import Industries, Hotels, Parks, Restaurants
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [ 
                url(r'^library/', ListView.as_view(
                                    queryset=Library.objects.all(),
                                    template_name="libraries/library.html")),
                url(r'^map/', ListView.as_view(
                                    queryset= maps.objects.all(),
                                    template_name="libraries/testmap.html")),
                url(r'^zoo/', ListView.as_view(
                                    queryset=Zoos.objects.all(),
                                    template_name="libraries/zoos.html")),
                url(r'^museum/', ListView.as_view(
                                    queryset=Museums.objects.all(),
                                    template_name="libraries/museum.html")),
                url(r'^college/', ListView.as_view(
                                    queryset=Colleges.objects.all(),
                                    template_name="libraries/college.html")),
                url(r'^mall/', ListView.as_view(
                                    queryset=Malls.objects.all(),
                                    template_name="libraries/mall.html")),
                url(r'^industry/', ListView.as_view(
                                    queryset=Industries.objects.all(),
                                    template_name="libraries/industry.html")),
                url(r'^hotel/', ListView.as_view(
                                    queryset=Hotels.objects.all(),
                                    template_name="libraries/hotel.html")),
                url(r'^park/', ListView.as_view(
                                    queryset=Parks.objects.all(),
                                    template_name="libraries/park.html")),
                url(r'^restaurant/', ListView.as_view(
                                    queryset=Restaurants.objects.all(),
                                    template_name="libraries/restaurant.html")),
  ##              url(r'^colleges/',
                ]

