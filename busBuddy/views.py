from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

def index(request):
    return HttpResponse("Hello, world.")

def login(request):
    context = {}
    template = loader.get_template('busBuddy/login.html')
    return HttpResponse(template.render(context, request))
