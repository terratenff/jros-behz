from django.urls import path

from . import views

app_name = 'secondfloor'
urlpatterns = [
    path('', views.index),
    path('about/', views.index),
    path('help/', views.index)
]
