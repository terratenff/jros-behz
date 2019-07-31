from django.urls import path

from . import views

app_name = 'secondfloor'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('people/', views.people, name='people'),
    path('groups/', views.groups, name='groups'),
    path('forum/', views.forum, name='forum'),
    path('events/', views.events, name='events'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('rules/', views.rules, name='rules'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('report_abuse/', views.report_abuse, name='reportabuse'),
    path('privacy_policy/', views.privacy_policy, name='privacypolicy'),
    path('feedback/', views.feedback, name='feedback'),
    path('customer_support/', views.customer_support, name='customersupport'),
    path('report_bug/', views.report_bug, name='reportbug'),
    path('search/', views.search, name='search')
]
