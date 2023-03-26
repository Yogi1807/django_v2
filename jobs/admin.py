from django.contrib import admin

# Register your models here.
from jobs.models import Portal, DjangoDB
admin.site.register(Portal)
admin.site.register(DjangoDB)
