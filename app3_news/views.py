from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def announcement(request): 
    template=loader.get_template('announcement.html')
    return HttpResponse(template.render())

def event(request): 
    template=loader.get_template('event.html')
    return HttpResponse(template.render())