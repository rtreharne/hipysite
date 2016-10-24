from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting, Beekeeper, Hive, Event, Sponsor
from datetime import datetime
from hello.forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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

def register(request, hive_id=1):

    event = Event.objects.get(id=hive_id)
    registrations = event.registrations

    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST)

        if registration_form.is_valid():
            reg = registration_form.save(commit=False)
            reg.event = event
            reg.save()
            registrations += 1
            event.registrations = registrations
            event.save()

            return HttpResponseRedirect('/#portfolio')
        else:
            print registration_form.errors
    else:
        registration_form = RegistrationForm

    return render (request, 'register.html', {'registration_form': registration_form, 'event':event})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

