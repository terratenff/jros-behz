from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from firstfloor.models import Profile

def index(request):
    """
    Index page.
    """
    return render(request, "firstfloor/index.html", context = None)

def login_prompt(request):
    """
    Site for logging in.
    """
    return render(request, "firstfloor/login_prompt.html", context = None)

@login_required(login_url = "firstfloor:login")
def profile(request):
    """
    Personal profile page. Must be logged in before the page
    can be viewed.
    """
    current_user = request.user
    profile = Profile.objects.get(user = current_user)

    # TODO
    profile_context = {}
    return render(request,
                  "firstfloor/profile.html",
                  context = profile_context)

def other_profile(request, name):
    """
    Site for viewing a profile other than user's own.
    """
    target_user = User.objects.get(username = name)
    profile = Profile.objects.get(user = target_user)

    # TODO
    profile_context = {}
    return render(request,
                  "firstfloor/index.html",
                  context = profile_context)
