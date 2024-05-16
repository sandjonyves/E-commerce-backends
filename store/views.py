from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.models import Permission ,Group

from rest_framework import viewsets,response
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.decorators import api_view,action,permission_classes
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny
# from rest_framework.parsers import MultiPartParser

from .serializers import *
from .models import *


class PierceViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer
    # parser_classes = [MultiPartParser]

    # @permission_classes([AllowAny])
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)
    # @permission_classes([AllowAny])
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    # @permission_classes([AllowAny])
    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)
    
    # permission_classes = [AllowAny]
    # @action(detail = False,methods=['get'],url_path = 'get_piece/(?P<id>\w+)')
    # def get_piece(self,request,id):
    #     queryset = Piece.objects.filter(id_cathegorie=id)
    #     data = list(queryset.values())
    #     return JsonResponse(data,safe=False)
       

class cathegorieViewSet(viewsets.ModelViewSet):

    queryset = Cathegorie.objects.all()
    serializer_class = CathegorieSerializer
    permission_classes=[AllowAny]
    # @permission_classes([IsAdminUser])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    # get all cathegorie of modele
    @action(detail=False, methods=['GET'], url_path='all-cathegorie-of-modele/(?P<model_id>\w+)')
    def read_all_Cathegorie_of_modele(self, request, modele_id):
        queryset = Cathegorie.objects.filter(modele_id = modele_id)
        data = list(queryset.values())
        return JsonResponse({'data': data, 'status': status.HTTP_200_OK}, safe=False)
    # @action(detail = False,methods=['get'],url_path = 'get_cathegorie/(?P<id>\w+)')
    # def get_cathegorie(self,request,id):
    #     queryset = Cathegorie.objects.filter(id_voiture=id)
    #     data = list(queryset.values())
    #     return JsonResponse(data,safe=False)
       
class CommandeViewSet(viewsets.ModelViewSet):
    serializer_class = CommandeSerializer
    queryset = Commande.objects.all()


# class commandeApiViews(generics.CreateAPIView):
#     serializer_class = CommandeSerializer
   
#     def post(self,request):

    # def perform_update(self, serializer):

    #     return super().perform_update(serializer)
class lists(generics.ListAPIView):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer



# Generic Update in server
# def generic_put(request, pk, obj, obj_serializer):
#     pass
# def update(self, request, obj, obj_serializer,*args, **kwargs):
#     partial = kwargs.pop('partial', False)
#     instance = self.get_object_or_none()
#     serializer = self.get_serializer(instance, data=request.data, partial=partial)
#     serializer.is_valid(raise_exception=True)

#     if instance is None:
#         lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
#         lookup_value = self.kwargs[lookup_url_kwarg]
#         extra_kwargs = {self.lookup_field: lookup_value}
#         serializer.save(**extra_kwargs)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     serializer.save()
#     return Response(serializer.data)
# @api_view(['PUT'])
# def batiment_edit(request,pk):
#     return update(request=request, pk=pk, obj=Piece, obj_serializer=PieceSerializer)
    

class SearchModelCathegorie(APIView):
    def get(self,request,id):
        queryset = Cathegorie.objects.filter(id_modele=id)
        data = list(queryset.values())
        
        return JsonResponse(data,safe=False)



class Read(viewsets.ViewSet):
    permission_classes=[AllowAny]
    @action(detail=False, methods=['GET'], url_path='all-cathegorie-of-modele/(?P<model_id>\w+)')
    def read_all_Cathegorie_of_modele(self, request, modele_id):
        queryset = Cathegorie.objects.filter(modele_id = modele_id)
        data = list(queryset.values())
        return JsonResponse({'data': data, 'status': status.HTTP_200_OK}, safe=False)
    
    @action(detail=False, methods=['GET'], url_path='all-piece-of-cathegorie/(?P<cathegorie_id>\w+)')
    def read_all_piece_of_cathegorie(self, request, cathegorie_id):
        """
        Returns a list of all pieces of a specific cathegorie.

        Parameters:
        -----------
        id_cathegorie (int): The id of the cathegorie.

        Returns:
        --------
        list: A list of all pieces of the specified cathegorie.

        """
        queryset = Piece.objects.filter(id_cathegorie=cathegorie_id)
        serializer = PieceSerializer(queryset,many=True,context = {'request':request})
        
        return Response(serializer.data)
    # @action(detail=False,methods = ['GET'],url_path='all-test-ue/(?P<ue_id>\w+)')

    @action(detail = False, methods=['GET'],url_path='all-commande-of-client/(?P<client_id>\w+)')
    def read_all_commande_of_client(self,request,client_id):
        queryset = Commande.objects.filter(client_id = client_id)
        data = list(queryset.values())

        return JsonResponse({'data': data,'status': status.HTTP_200_OK}, safe=False)


    @action(detail=False,methods=['GET'],url_path = "piece-of-cathegorie/(?P<piece_id>\w+)/(?P<cathegorie_id>\w+)")
    def piece_of_cathegorie(self,request,piece_id,cathegorie_id):
        query = Piece.objects.filter(id=piece_id,id_cathegorie = cathegorie_id)
        serializer = PieceSerializer(query,many=True, context= {"request":request})
        return Response(serializer.data)
    # @action(detail=False, methods=['GET'], url_path='all-piece-of-commande/(?P<id_commande>\w+)/')
    # def read_all_cathegorie_of_piece(self, request, id_piece):