from django.contrib import admin
from facilities.models import *
# Register your models here.
from django.contrib.gis import admin

admin.site.register(Facility)
admin.site.register(OperationStatus)
admin.site.register(FacilityType)
