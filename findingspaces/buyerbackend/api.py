from buyerbackend.models import BuyerBackend
from rest_framework import viewsets, permissions
from .serializers import BuyerSerializer

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = BuyerBackend.objects.all()
    permission_classes = [
        permissions.AllowAny
        ]
    serializer_class = BuyerSerializer
