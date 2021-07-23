from rest_framework import serializers
from buyerbackend.models import BuyerBackend

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerBackend
        fields = '__all__'