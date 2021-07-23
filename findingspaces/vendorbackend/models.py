from django.db import models

class VendorBackend(models.Model):
    vendor_id = models.IntegerField()
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    rating = models.IntegerField()
    