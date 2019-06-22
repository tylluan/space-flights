from rest_framework import serializers
from .models import Flights, Tourists


class TouristsSerializer(serializers.ModelSerializer):
    """
    Serializer for Tourists model
    """
    class Meta:
        model = Tourists
        fields = '__all__'


class FlightsSerializer(serializers.ModelSerializer):
    """
    Serializer for Flights model
    """

    class Meta:
        model = Flights
        fields = '__all__'
