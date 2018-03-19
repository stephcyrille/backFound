from rest_framework import serializers

from .models import PoliceStation, Cni, Recep


class PoliceStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceStation
        fields = ('name', 'region', 'city', 'lat', 'long')


class CniSerializer(serializers.ModelSerializer):
    address = PoliceStationSerializer(required=True)

    class Meta:
        model = Cni
        fields = ('nberCni', 'name', 'surname', 'birthdate', 'address')
    

class RecepSerializer(serializers.ModelSerializer):
    address = PoliceStationSerializer(required=True)

    class Meta:
        model = Recep
        fields = ('nberRecep', 'name', 'surname', 'birthdate', 'address')
