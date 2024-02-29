from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.http import JsonResponse
from .models import *
from .serializer import *
from django.db.models import F
# Create your views here.

class MarqueViewSet(viewsets.ModelViewSet):
    queryset = Marque.objects.all()
    serializer_class= MarqueSerializer

class ModeleViewSet(viewsets.ModelViewSet):
    queryset = Modele.objects.all()
    serializer_class= ModeleSrializer

class VoitureViewSet(viewsets.ModelViewSet):
    queryset = Voiture.objects.all()
    serializer_class = VoitureSerializer

class ReadMarque(APIView):
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
    def get(self,request,id):
        #joiture entre les trois tables voiture modele et marque en fonction de leurs ID
        queryset = Voiture.objects.filter(id_modele__id_marque_id = id)
        #transformation sous forme de liste et renommager de certains champs
        data  = list(queryset.values('id','name','id_modele',modele_nama =  F('id_modele__name'),marque_name =  F('id_modele__id_marque__name')))
        #retournement sous forme de Json
        return JsonResponse(data,safe=False)

