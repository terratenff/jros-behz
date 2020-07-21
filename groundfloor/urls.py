"""groundfloor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstfloor.urls')),
    path('toolbox/', include('secondfloor.urls')),
    # path('forum/', include('thirdfloor.urls')),
    path('', views.index, name='index'),
    path('a_profile/', views.profile, name='profile'),
    path('a_people/', views.people, name='people'),
    path('a_groups/', views.groups, name='groups'),
    path('forum/', views.forum, name='forum'),
    path('a_events/', views.events, name='events'),
    path('a_login/', views.login, name='login'),
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
