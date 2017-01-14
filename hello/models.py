from django.db import models
from sorl.thumbnail import ImageField
from datetime import datetime

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Beekeeper(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)
    thumbnail = ImageField(upload_to='beekeeper_thumb', null=True, blank=True)

    def __unicode__(self):
        return self.last_name

class Hive(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=140)
    thumbnail = ImageField(upload_to='hive_thumb', null=True, blank=True)
    description = models.TextField(max_length=1000, null = True, blank=True)

    def __unicode__(self):
        return self.title

class Event(models.Model):
    hive = models.ForeignKey(Hive)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField(null=False)
    location = models.CharField(max_length=50)
    registrations = models.IntegerField(default=0)
    stats = models.ImageField(upload_to='stats', null=False, blank=True)
    photos = models.URLField(blank=True, null=False)
    playlist = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.hive.title

class Sponsor(models.Model):
    title = models.CharField(max_length=25)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    url = models.URLField(null=True)

    def __unicode__(self):
        return self.title

class Registration(models.Model):

    event = models.ForeignKey(Event)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    department = models.CharField(max_length=25)
    email = models.EmailField()
    profile = models.URLField(null=True, blank=True)
    song = models.CharField(max_length=50, blank=True)
    timestamp = models.DateTimeField(default=datetime.now())

class Resource(models.Model):
    hive = models.ForeignKey(Hive)
    description = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.description



