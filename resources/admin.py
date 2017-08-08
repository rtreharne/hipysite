from django.contrib import admin
from resources.models import *

class ElementAdmin(admin.ModelAdmin):
    model = Element
    list_display = ('title', 'module', 'description')
    prepopulated_fields = {'slug': ['title'],}

class ModuleAdmin(admin.ModelAdmin):
    model = Module
    list_display = ('title', 'description')
    prepopulated_fields = {'slug': ['title'],}

admin.site.register(Module, ModuleAdmin)
admin.site.register(Element, ElementAdmin)


