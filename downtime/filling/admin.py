from django.contrib import admin

# Register your models here.

from .models import Park, Sample, Equip, Failure_сategory, Downtime

admin.site.register(Park)
admin.site.register(Sample)
admin.site.register(Equip)
admin.site.register(Failure_сategory)
admin.site.register(Downtime)
