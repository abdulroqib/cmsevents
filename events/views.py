from django.shortcuts import render
from .models import Events
from datetime import datetime

def index(request):
    featured_events = Events.objects.filter(is_featured=True)
    context = {
        'title': 'Featured Events',
        'featured_events': featured_events
    }
    return render(request, 'events/index.html', context)

def events(request):
    events = Events.objects.filter(datetime__gte=datetime.now())
    context = {
        'title': 'Upcoming Events',
        'events': events
    }
    return render(request, 'events/events.html', context)

def past_events(request):
    past_events = Events.objects.filter(datetime__lt=datetime.now())
    context = {
        'title': 'Past Events',
        'past_events': past_events
    }
    return render(request, 'events/past-events.html', context)

def detail(request, id):
    event = Events.objects.get(id=id)
    context = {
        'event': event
    }
    return render(request, 'events/detail.html', context)