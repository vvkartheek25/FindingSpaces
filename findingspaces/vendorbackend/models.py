from django.db import models

class VendorBackend(models.Model):
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)