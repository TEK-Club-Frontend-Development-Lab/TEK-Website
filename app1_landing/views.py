from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def landing(request): 
    template=loader.get_template('landing.html')
    return HttpResponse(template.render())

def modal(request):
    template=loader.get_template('modal.html')
    return HttpResponse(template.render())