# -*- encoding: utf-8 -*-
""" Home urls """

from django.conf.urls import url
from . import views

# Agregamos nuestras urls de la app
urlpatterns = [
    url(r'^hello_world/$', views.hello_world, name='hello_world'),
]
