from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt import authentication
from .models import *
from .serializer import *
from django.db.models import F
# Create your views here.

class MarqueViewSet(viewsets.ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Marque.objects.all()
    serializer_class= MarqueSerializer


class ModeleViewSet(viewsets.ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Modele.objects.all()
    serializer_class= ModeleSrializer

# class VoitureViewSet(viewsets.ModelViewSet):
#     queryset = Voiture.objects.all()
#     serializer_class = VoitureSerializer


class SearchModeleMarque(APIView):
    @action(detail=False,methods=['get'],url_path='all-modele-of-marque')
    def get_all_modele_marque(self,request,id):
        #joiture entre les trois tables voiture modele et marque en fonction de leurs ID
        queryset = Modele.objects.filter(id_marque__id = id)
        #transformation sous forme de liste et renommager de certains champs
        data  = list(queryset.values('id','name',marque_name =  F('id_marque__name')))
        #retour des donnees  sous forme de Json
        return JsonResponse(data,safe=False)
    # queryset = Voiture.objects.all()
    # serializer_class = VoitureSerializer
    #affichage de tous les marques des voitures 
    # @action(detail=False,methods=['get'],url_path='get_marque')
    # def get_marque(self,rquest):
    #     #recuperation de tout les marques 
    #     query = Marque.objects.all()
    #     #tranformation des donnees  sous formes de liste
    #     data = list(query.values('id','name'))
    #     #retournement sous forme de Json
    #     return JsonResponse(data,safe=False)
    
    # @action(detail=False,methods=['get'],url_path="search/(?P<id>\w+)")


