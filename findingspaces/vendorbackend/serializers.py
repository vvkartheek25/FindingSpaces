# from findingspaces.vendorbackend.models import VendorBackend
# from django.db import models
# from django.db.models import fields
from rest_framework import serializers
from vendorbackend.models import VendorBackend

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorBackend
        fields = '__all__'