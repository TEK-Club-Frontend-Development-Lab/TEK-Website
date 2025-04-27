from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def apply(request): 
    template=loader.get_template('apply.html')
    return HttpResponse(template.render())


def contact(request): 
    template=loader.get_template('contact.html')
    return HttpResponse(template.render())


def faq(request): 
    template=loader.get_template('faq.html')
    return HttpResponse(template.render())