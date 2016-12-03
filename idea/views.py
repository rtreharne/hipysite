from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def idea(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'idea.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

