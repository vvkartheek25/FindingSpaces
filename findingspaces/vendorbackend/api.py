from vendorbackend.models import VendorBackend
from rest_framework import viewsets, permissions
from .serializers import VendorSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = VendorBackend.objects.all()
    permission_classes = [
        permissions.AllowAny
        ]
    serializer_class = VendorSerializer
