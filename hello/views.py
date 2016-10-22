from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting, Beekeeper, Hive, Event, Sponsor
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    hives = Hive.objects.all()
    events = []
    events = Event.objects.filter(finish_time__gte=now).order_by('start_time')
    event_sub = events[:min(len(events), 3)]
    beekeepers = Beekeeper.objects.all()
    sponsors = Sponsor.objects.all()
    
    return render(request, 'index.html', {'hives': hives, 'events': event_sub, 'beekeepers': beekeepers, 'sponsors': sponsors})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

