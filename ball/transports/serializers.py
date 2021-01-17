from rest_framework import serializers
from .models import TransportFieldsModel


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportFieldsModel
        fields = '__all__'



