"""data_visualiser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from data_visualiser.views import homepage
from data_visualiser.api import (MaxTempResource, MinTempResource,
                MeanTempResource, RainDataResource, SunshineDataResource)
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(MaxTempResource())
v1_api.register(MinTempResource())
v1_api.register(MeanTempResource())
v1_api.register(RainDataResource())
v1_api.register(SunshineDataResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name="homepage"),
    url(r'^django-rq/', include('django_rq.urls')),
    url(r'^api/', include(v1_api.urls)),
]
