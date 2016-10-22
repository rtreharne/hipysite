from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Beekeeper

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    beekeepers = Beekeeper.objects.all()
    return render(request, 'index.html', {'beekeepers': beekeepers})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

