from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Beekeeper(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    twitter = models.URLField(null=True)
    facebook = models.URLField(null=True)
    linkedIn = models.URLField(null=True)
    thumbnail = ImageField(upload_to='beekeeper_thumb', null=True, blank=True)

    def __unicode__(self):
        return self.last_name

class Hive(models.Model):
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

    def __unicode__(self):
        return self.hive.title
