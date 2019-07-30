from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from firstfloor.models import Profile

def index(request):
    """
    Index page.
    """
    return render(request, "secondfloor/index.html", context = None)

# TODO: Views for the following (ignore duplicates):
# Home
# Profile
# People
# Groups
# Forum
# Events
# Log In / Log Out

# Home
# Profile
# About
# Contact
# Help
# Rules
# Guidelines
# Report Abuse
# Privacy Policy
# Feedback
# Customer Support
# Report a Bug
