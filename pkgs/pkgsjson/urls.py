from django.urls import path


from django.urls import path
from . import views


urlpatterns = [
    path('json', views.json, name='app-json'),
    path('html', views.json, name='app-html'),
]