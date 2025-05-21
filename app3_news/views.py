from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import calendar
from datetime import datetime
from .models import Event

def announcement(request): 
    template=loader.get_template('announcement.html')
    return HttpResponse(template.render())

def event(request): 
    
    now = datetime.now()
    year = now.year
    month = now.month
    month_name = now.strftime('%B') 

    calendar.setfirstweekday(calendar.MONDAY)
    cal = calendar.monthcalendar(year, month)
    events = Event.objects.all() 

    context = {
        'month_name': month_name,
        'cal': cal,
        'year': year,
        'month': month,
        'events': events,
    }

    return render(request, 'event.html', context)
