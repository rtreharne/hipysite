from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting, Beekeeper, Hive, Event, Sponsor, Registration, Resource
from datetime import datetime
from hello.forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def regCheck(event, registration):
    if Registration.objects.filter(email=registration.email, event=event):
        return True
    return False

# Create your views here.
def index(request):
    now = datetime.now()
    hives = Hive.objects.all()
    events = []
    events = Event.objects.filter(hive__project__title='hipy', finish_time__gte=now).order_by('start_time')
    past_events = Event.objects.filter(finish_time__lte=now).order_by('-start_time')
    registrations = Registration.objects.all()
    email_list = set([x.email for x in registrations])
    email_string = ",".join(email_list)
    registrations = Registration.objects.all().order_by('last_name')
    resources = []
    resources = Resource.objects.all()
    event_sub = events[:min(len(events), 6)]
    beekeepers = Beekeeper.objects.all()
    sponsors = Sponsor.objects.all()
    
    return render(request, 'index.html', {'hives': hives,
                                          'events': event_sub,
                                          'beekeepers': beekeepers,
                                          'sponsors': sponsors,
                                          'registrations': registrations,
                                          'resources': resources,
                                          'past_events': past_events,
                                          'emails': email_string,
                                          'emails_len': len(email_list)})

def promo(request):
    now = datetime.now()
    events = Event.objects.filter(finish_time__gte=now).order_by('start_time')
    return render(request, 'promo.html', {'events': events})

def hive(request, hive_id=1):
    event = Event.objects.get(id=hive_id)
    registrations = Registration.objects.all().order_by('last_name')
    resources = Resource.objects.all()

    return render(request, 'hive.html', {'event': event,
                                         'registrations': registrations,
                                         'resources': resources,
                                         })


def register(request, hive_id=1):

    event = Event.objects.get(id=hive_id)
    registrations = event.registrations
    submitted = None

    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST)

        if registration_form.is_valid():
            reg = registration_form.save(commit=False)
            reg.event = event
            # perform registration check
            if regCheck(event, reg):
                submitted = 'Dude, you already registered!'
            else:
                reg.save()
                registrations += 1
                event.registrations = registrations
                event.save()
                submitted = 'Congratulations! You have registered.'
            return render(request, 'register.html', {'event':event, 'regData': reg, 'registration_form': registration_form, 'submitted':submitted})
        else:
            print registration_form.errors
    else:
        registration_form = RegistrationForm

    return render (request, 'register.html', {'registration_form': registration_form, 'event':event, 'submitted': submitted})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

