from django.contrib import admin
from hello.models import Beekeeper, Event, Hive, Sponsor, Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'first_name', 'last_name', 'email')

admin.site.register(Beekeeper)
admin.site.register(Event)
admin.site.register(Hive)
admin.site.register(Sponsor)
admin.site.register(Registration, RegistrationAdmin)

# Register your models here.
