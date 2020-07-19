from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

def index(request):
    """
    Index page. Acts as the home page of the website.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def profile(request):
    """
    General Profile page. Extensive profile page can be found
    from 'firstfloor'.

    TODO: Move this to 'firstfloor'.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def people(request):
    """
    People page. Contains a search bar that can be used
    to find people.

    TODO: Move this to 'firstfloor'.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def groups(request):
    """
    Group page. Contains a list of popular 'public'
    groups, and a search bar for finding more. Also contains
    a button for creating a group (requires logging in).

    TODO: Move this to 'firstfloor'.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def forum(request):
    """
    Forum Entrance page. Contains an introduction to the
    forum itself.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def events(request):
    """
    Events page. Contains a short list of popular 'public'
    events, and a search bar for finding more. Also contains
    a button for creating an event (requires logging in).

    TODO: Move this to 'firstfloor'.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def login(request):
    """
    General Login page. Contains the option to sign in to an
    existing account, and the option to create a new one.

    TODO: Move this to 'firstfloor'.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def about(request):
    """
    About page. Contains general information about the website.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def contact(request):
    """
    Contact page. Contains contact information.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def help(request):
    """
    Help page. Contains information on how to get started with
    the website.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def rules(request):
    """
    Rules page. Contains a set of rules that have to be followed.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def guidelines(request):
    """
    Guidelines page. Contains a set of guidelines that people
    are encouraged to follow within the website.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def report_abuse(request):
    """
    Report Abuse page. Here one can report another for a
    potential rule violation.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def privacy_policy(request):
    """
    Privacy Policy page. Contains the privacy statement (just
    GDPR things).
    """

    return render(request, "groundfloor/common/index.html", context = None)

def feedback(request):
    """
    Feedback page. Here one can send feedback to improve the
    website further.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def customer_support(request):
    """
    Customer Support page. Contains information that aims
    to solve a variety of technical issues (within the website),
    and the means to contact tech support if the problem
    is too specific.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def report_bug(request):
    """
    Report Bug page. Here one can report technical problems
    with the website.
    """

    return render(request, "groundfloor/common/index.html", context = None)

def search(request):
    """
    General Search page. Contains a search bar that one can
    use to find something.

    If POST-information could be found, shows search results
    as well.
    """

    return render(request, "groundfloor/common/index.html", context = None)
