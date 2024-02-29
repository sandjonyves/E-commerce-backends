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
    # piece = PieceSerializer (many = True)
    # multiple_piece_commande = serializers.ListField(
    #     child = PieceSerializer(many = True),
    #     write_only = True 
    # )
    class Meta:
        model = Commande
        fields ='__all__'

    # def create(self, validated_data):
    #     multiple_piece_commande = validated_data.pop('multiple_piece_commande')
    #     commande = Commande.objects.create(**validated_data)
    #     for pieces in multiple_piece_commande:
    #         nem_piece = Piece.objects.create(Commande)