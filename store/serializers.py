from rest_framework import serializers
from .models import *



class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields ='__all__'
    
class CathegorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cathegorie
        fields ='__all__'

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields ='__all__'
