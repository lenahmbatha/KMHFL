from django.db import models
from maps.models import District, Constituency, Ward, LocationType

# Create your models here.

class OperationStatus(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Operation Status"


class FacilityType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self): 
        return self.name

    # class Meta:
    #     verbose_name_plural = "Facility Types"
        
class Facility(models.Model):
    name = models.CharField(max_length=100)
    facility_type = models.ForeignKey(FacilityType, on_delete=models.DO_NOTHING)
    operation_status = models.ForeignKey(OperationStatus, on_delete=models.DO_NOTHING, default=1)
    number_of_beds = models.IntegerField(null=True, blank=True)
    number_of_nurses = models.IntegerField(null=True, blank=True)
    number_of_doctors = models.IntegerField(null=True, blank=True)
    address_line1 = models.CharField(max_length=60, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    constituency = models.ForeignKey(Constituency, on_delete=models.DO_NOTHING, null=True, blank=True)
    ward = models.ForeignKey(Ward, on_delete=models.DO_NOTHING, null=True, blank=True)
    location_type = models.ForeignKey(LocationType, on_delete=models.DO_NOTHING, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    mobile = models.CharField(max_length=13, null=True, blank=True)
    rated = models.TextField(max_length=1000, null=True, blank=True)
    rating = models.TextField(max_length=10, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    slug = models.SlugField(max_length=254, null=True, blank=True)


