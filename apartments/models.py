from django.db import models

# Create your models here.
class Apartment(models.Model):
    apartment_name = models.CharField(max_length=200)
    access_type = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    total_occupancy = models.IntegerField(default=0)

all_apartments = Apartment.objects.all()
print(all_apartments)