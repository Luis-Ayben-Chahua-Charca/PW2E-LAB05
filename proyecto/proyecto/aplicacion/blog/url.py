from django import views
from django.urls import path
from . import views
urlpatterns =[
	path("", views.home),
	path("registrar/", views.registrar),
	path("eliminar/<titulo>",views.eliminar),
	path("modificar/<titulo>",views.modificar),
	path("modificarblog/",views.modificarblog),
]