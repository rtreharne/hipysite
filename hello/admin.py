from django.contrib import admin
from hello.models import Beekeeper, Event, Hive, Sponsor, Registration, Resource

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'first_name', 'last_name', 'email')

class ResourceAdmin(admin.ModelAdmin):
    list_display =('hive', 'description', 'link')

admin.site.register(Beekeeper)
admin.site.register(Event)
admin.site.register(Hive)
admin.site.register(Sponsor)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Resource, ResourceAdmin)

# Register your models here.
