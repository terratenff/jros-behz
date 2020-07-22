from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from firstfloor.models import Profile

def login_prompt(request):
    """
    General Login page. Contains the option to sign in to an
    existing account, and the option to create a new one.
    """

    # TODO

    if "next" in request.GET:
        destination = request.GET["next"]
        return render(request, "firstfloor/login_prompt.html", context = {"next": destination})
    else:
        return render(request, "firstfloor/login.html", context = None)

def login(request):
    """
    This view conducts the act of logging in.
    """

    # TODO: Collect "next" value from POST if it exists.

    return render(request, "firstfloor/login.html", context = None)

def logout(request):
    """
    Site for logging out.
    """

    # TODO

    return render(request, "firstfloor/logout.html", context = None)

@login_required(login_url = "firstfloor:login_prompt")
def profile_overview(request):
    """
    General Profile page. Extensive profile page can be found
    by specifying target username.
    """

    current_user = request.user
    profile = Profile.objects.get(user = current_user)

    # TODO

    profile_context = {}
    return render(request,
                  "firstfloor/profile_overview.html",
                  context = profile_context)

@login_required(login_url = "firstfloor:login_prompt")
def profile(request, profilename):
    """
    Site for viewing a profile.
    """

    target_user = User.objects.get(username = profilename)
    profile = Profile.objects.get(user = target_user)

    # TODO

    profile_context = {}
    return render(request,
                  "firstfloor/profile.html",
                  context = profile_context)

@login_required(login_url = "firstfloor:login_prompt")
def people(request):
    """
    People page. Contains a search bar that can be used
    to find people.
    """

    # TODO

    return render(request, "firstfloor/people.html", context = None)

def groups(request):
    """
    Group page. Contains a list of popular 'public'
    groups, and a search bar for finding more. Also contains
    a button for creating a group (requires logging in).
    """

    # TODO

    return render(request, "firstfloor/groups.html", context = None)

def events(request):
    """
    Events page. Contains a short list of popular 'public'
    events, and a search bar for finding more. Also contains
    a button for creating an event (requires logging in).
    """

    # TODO

    return render(request, "firstfloor/events.html", context = None)
