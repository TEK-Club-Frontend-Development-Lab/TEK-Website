from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def signin(request): 
    template=loader.get_template('signin.html')
    return HttpResponse(template.render())

def signup(request): 
    template=loader.get_template('signup.html')
    return HttpResponse(template.render())

def mypage(request): 
    template=loader.get_template('mypage.html')
    return HttpResponse(template.render())