from django.contrib import admin
from .models import Province, District, Constituency, Ward, DistrictType, LocationType
# Register your models here.
admin.site.register(District)
admin.site.register(Constituency)
admin.site.register(Ward)
admin.site.register(DistrictType)
admin.site.register(LocationType)