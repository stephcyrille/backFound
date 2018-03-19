from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^cnis/(?P<cniNber>[0-9]+)/$', CniDetail.as_view()),
    url(r'^recep/(?P<recepNber>[\w-]+)/$', RecepDetail.as_view()),
    url(r'^cnis/advanced/(?P<name>[\w-]+)/(?P<surname>[\w-]+)/(?P<birthdate>[\w-]+)/$', CniAdvancedDetail.as_view()),
]