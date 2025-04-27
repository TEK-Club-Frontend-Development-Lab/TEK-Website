from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def lab1(request): 
    template=loader.get_template('lab1.html')
    return HttpResponse(template.render())

def lab2(request): 
    template=loader.get_template('lab2.html')
    return HttpResponse(template.render())

def lab3(request): 
    template=loader.get_template('lab3.html')
    return HttpResponse(template.render())

def lab4(request): 
    template=loader.get_template('lab4.html')
    return HttpResponse(template.render())