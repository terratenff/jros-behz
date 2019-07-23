from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

def index(request):
    return render(request, "secondfloor/index.html", context = None)
