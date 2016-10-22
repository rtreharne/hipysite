from django.db import models

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

