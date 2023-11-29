from django.urls import path

from . import views

app_name = 'filling'

urlpatterns = [
    path('', views.filling, name='filling'),
]