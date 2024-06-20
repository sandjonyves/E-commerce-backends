from rest_framework import serializers
from store.models import *
from app.serializer import MarqueSerializer
from account.serializer import OtherClientSerializer
import json

class PieceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieceImage
        fields = '__all__'

class PieceSerializer(serializers.ModelSerializer):
    thumbs = PieceImageSerializer(many=True,read_only=True)
    # thumbs = serializers.SerializerMethodField()
    # images= serializers.ListField(
    #             child = serializers.ImageField(max_length =1000000,allow_empty_file=False,
    #                                           use_url = False),
    #                                            write_only=True
    #                                            )    
    images = serializers.ListField( 
                                    child = serializers.CharField(),
                                    max_length =255,
                                    write_only=True)
    
    marque = MarqueSerializer(source='id_marque', read_only=True)
                             
    class Meta:
        model = Piece
        fields =('id','id_marchand','id_cathegorie','id_marque','marque','modele','name','price','qt_stock','city','description','images','thumbs')
    def create(self, validated_data):
        piece_images = validated_data.pop('images')

        piece = Piece.objects.create(**validated_data)

        for piece_image in piece_images:
            image = json.loads(piece_image)
            PieceImage.objects.create(thumbs=piece,image_url=image['url'],public_id=image['public_id'])

        return piece

    # def get_marque(self,validate_data):

    #     id_marque = validate_data['id_marque']
    #     queryset = Marque.objects.get(id = id_marque)
    #     return MarqueSerializer(queryset).data
    
    def get_thumbs(self,instace):

        queryset = instace.pieceImage.all()
        request = self.context.get('request')
        serializers = PieceImageSerializer(queryset,context={'request':request})
        return serializers.data


class CathegorieSerializer(serializers.ModelSerializer):
    pieces =serializers.SerializerMethodField()
    class Meta:
        model = Cathegorie
        fields = ('id','name','thumbs','pieces')

    def create(self, validated_data):
        
        # pieces = validated_data.pop('pieces')
        # print(validated_data)
        queryset = Cathegorie.objects.create(**validated_data)
        return queryset
    
    def get_pieces(self,instance):
        queryset = instance.pieces.all()
        request= self.context.get('request')
        serializers = PieceSerializer(queryset,many=True,context = {'request':request})
        return serializers.data
    
class CommandeSerializer(serializers.ModelSerializer):

    client =OtherClientSerializer(source="client_id",read_only=True)
    pieces =serializers.SerializerMethodField()

    class Meta:
        model = Commande
        fields =(
                'id',
                'total_price',
                 'commande_date',
                 'status',
                 'operator',
                 'transaction_id',
                 'piece',
                 'client_id',
                 'piece_qte',
                 'client',
                 'pieces'
                )

    # def get_client(self,instance):
    #     queryset = instance.client_id.get()
    #     request= self.context.get('request')
    #     serializers = OtherClientSerializer(queryset,many=True,context = {'request':request})
    #     return serializers.data
    def get_pieces(self,instance):
        queryset = instance.piece.all()
        request= self.context.get('request')
        serializers = PieceSerializer(queryset,many=True,context = {'request':request})
        return serializers.data
    # def create(self, validated_data):
    #     multiple_piece_commande = validated_data.pop('multiple_piece_commande')
    #     commande = Commande.objects.create(**validated_data)
    #     for pieces in multiple_piece_commande:
    #         nem_piece = Piece.objects.create(Commande)
