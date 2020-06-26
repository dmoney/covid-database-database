from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Source)
admin.site.register(models.Field)
admin.site.register(models.Scope)
