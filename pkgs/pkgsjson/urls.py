from django.urls import path
from . import views

urlpatterns = [
    path('json', views.jsonraw, name='app-json'), #calling it literally 'json' causes packages to not load
    path('html', views.html, name='app-html'),
]