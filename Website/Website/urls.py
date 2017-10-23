"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

# Add this import
from django.contrib.auth import views
from log.forms import LoginForm
from student.views import enter_view

urlpatterns = [
    url(r'^enter/', enter_view, name='enter_view'),
    url(r'^registration/', include('registration.urls')),
    url(r'^home/', include('log.urls')),
    url(r'^login/$', views.login, {'template_name': 'log/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/'}),  
    url(r'^webapp/', include('webapp.urls')),
    url(r'^', include('Personal.urls')),
    url(r'^login/', include('authentication.urls')), 
    url(r'^student/', include('student.urls')), 
    url(r'^businessman/', include('businessman.urls')),
    url(r'^tourist/', include('tourist.urls')),
    url(r'^resources/', include('libraries.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
