from django.urls import path

from . import views

app_name = 'firstfloor'
urlpatterns = [
    path('login/', views.login_prompt, name='login_prompt'),
    path('logging-in/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile_overview, name='profile_overview'),
    path('profile/<str:profilename>/', views.profile, name='profile'),
    #path('profile/<str:username>/friend-list/', views.profile_friend_list, name='friend_list'),
    #path('profile/<str:username>/friend-requests/', views.profile_friend_requests, name='friend_requests'),
    path('people/', views.people, name='people'),
    path('groups/', views.groups, name='groups'),
    path('events/', views.events, name='events')
]
