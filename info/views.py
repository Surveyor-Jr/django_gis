from django.shortcuts import render
from django.http.response import Http404
from django.http import HttpResponse, HttpResponseNotFound


def LandingPage(request):
    return render(request, 'landing_page.html')


def ErrorPage(request):
    return render(request, 'error.html')
