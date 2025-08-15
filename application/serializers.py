from rest_framework import serializers
from .models import *

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'

class PressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure
        fields = '__all__'

class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = '__all__'

class DewPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DewPoint
        fields = '__all__'

class WindSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindSpeed
        fields = '__all__'