from django.contrib import admin
from hello.models import Beekeeper, Event, Hive, Sponsor

admin.site.register(Beekeeper)
admin.site.register(Event)
admin.site.register(Hive)
admin.site.register(Sponsor)

# Register your models here.
