from django.urls import path

from . import views

app_name = 'firstfloor'
urlpatterns = [
    path('firstfloorindex/', views.index, name = 'index'),
    path('firstfloorlogin/', views.login_prompt, name = 'login'),
    path('firstfloorprofile/', views.profile, name = 'profile'),
    path('firstfloorprofile/<name>/', views.other_profile, name = 'other_profile')
]
