from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Greeting, Beekeeper, Hive, Event, Sponsor, Registration, Resource
from datetime import datetime

from .models import Greeting

# Create your views here.
def idea(request):
    now = datetime.now()
    hives = Hive.objects.all()
    events = []
    events = Event.objects.filter(hive__project__title='idea', finish_time__gte=now).order_by('start_time')
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

    return render(request, 'idea.html', {'hives': hives,
                                          'events': event_sub,
                                          'beekeepers': beekeepers,
                                          'sponsors': sponsors,
                                          'registrations': registrations,
                                          'resources': resources,
                                          'past_events': past_events,
                                          'emails': email_string,
                                          'emails_len': len(email_list)})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

