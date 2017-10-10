from django.db import models
from sorl.thumbnail import ImageField
from datetime import datetime
from hello.models import Beekeeper

class Module(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    coordinator = models.ForeignKey(Beekeeper)
    description = models.TextField(max_length=10000)
    thumbnail = ImageField(upload_to='module_thumb', null=True, blank=True)
    live = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.title

class Element(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    module = models.ForeignKey(Module, null=True, blank=True)
    description = models.TextField(max_length=10000)
    github_link = models.URLField(null=True, blank=True)
    azure_link = models.URLField(null=True, blank=True)
    cocalc_link = models.URLField(null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)
    prev_item = models.ForeignKey("self", null=True, blank=True)
    next_item = models.ForeignKey("self", null=True, blank=True, related_name='+')
    recommended = models.ManyToManyField("self", null=True, blank=True)

    def __unicode__(self):
        return self.title