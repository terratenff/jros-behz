from django.urls import path

from . import views

app_name = 'firstfloor'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login_prompt, name = 'login'),
    path('profile/', views.profile, name = 'profile'),
    path('profile/<name>/', views.other_profile, name = 'other_profile')
]
