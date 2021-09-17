from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_header = "MicroTasks Admin"
admin.site.site_title = "Micro Admin Portal"
admin.site.index_title = "Welcome to MicroTasks"


admin.site.register(models.Event)
admin.site.register(models.Performer)
admin.site.register(models.Profile)