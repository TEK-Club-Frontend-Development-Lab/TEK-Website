from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def regulation(request): 
    template=loader.get_template('regulation.html')
    return HttpResponse(template.render())