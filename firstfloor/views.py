from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from firstfloor.models import Profile

def login_prompt(request):
    """
    General Login page. Contains the option to sign in to an
    existing account, and the option to create a new one.
    """

    try:
        destination = request.GET["next"]
    except KeyError:
        destination = "/profile_overview/"

    return render(request, "firstfloor/login.html", context = {"next": destination})

def login(request):
    """
    This view conducts the act of logging in.
    """

    if request.method == "POST":
        destination = request.POST["login-destination"]
        username = request.POST["login-username"]
        password = request.POST["login-password"]

        logged_user = authenticate(username=username, password=password)
        if logged_user is not None:
            dj_login(request, logged_user)
            return redirect(destination)
        else:
            login_error = "Invalid username/password."
            return render(request, "firstfloor/login.html", context = {"next": destination, "error": login_error})
    else:
        render(request, "firstfloor/login.html", context = {"next": destination})

def new_account_prompt(request):
    """
    General Account creation page. Contains various fields where
    user must input necessary data to create an account.
    """

    return render(request, "firstfloor/new_account.html", context = None)

def new_account(request):
    """
    This view conducts the act of creating a new account.
    """

    if request.method == "POST":
        new_username = request.POST["new-username"]
        new_password = request.POST["new-password"]
        new_repeat_password = request.POST["new-repeat-password"]
        new_firstname = request.POST["new-firstname"]
        new_lastname = request.POST["new-lastname"]
        new_email = request.POST["new-email"]

        if new_password == new_repeat_password:
            new_user = User.objects.create_user(new_username, new_email, new_password)
            new_user.first_name = new_firstname
            new_user.last_name = new_lastname
            dj_login(request, new_user)
            new_profile = Profile.objects.create(user=new_user)
            return redirect(reverse("firstfloor:profile_overview"))
        else:
            error_text = "Given passwords do not match."
            return render(request, "firstfloor/new_account.html", context = {"error": error_text})
    else:
        return render(request, "firstfloor/new_account.html", context = None)

    new_user = User.objects.create("username", "email@email.com", "password")
    new_user.first_name = "firstname"
    new_user.last_name = "lastname"
    new_profile = Profile.objects.create(user=new_user)

    return redirect(reverse("firstfloor:profile_overview"))

def logout(request):
    """
    Logs out the user.
    """

    dj_logout(request)
    messages.add_message(request, messages.SUCCESS, "You have logged out successfully!")
    return redirect(reverse("firstfloor:login_prompt"))

def logout_landing(request):
    """
    The landing site upon logging out.
    """

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
