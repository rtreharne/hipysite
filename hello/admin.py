from django.contrib import admin
from hello.models import Beekeeper, Event, Hive

admin.site.register(Beekeeper)
admin.site.register(Event)
admin.site.register(Hive)

# Register your models here.
