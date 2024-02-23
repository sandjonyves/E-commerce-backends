from rest_framework import serializers
from .models import *


class MarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marque
        fields = '__all__' 

class ModeleSrializer(serializers.ModelSerializer):
    class Meta:
        model= Modele
        fields = '__all__'

class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Voiture
        fields = '__all__'