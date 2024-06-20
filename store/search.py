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

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .models import *




class CommandeSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client_id__email','client_id__phone_number','transaction_id']


class PieceSearch(generics.ListAPIView):
    permission_class =[AllowAny]
    querytset  = Piece.objects.all()
    serialiezer_class = PieceSerializer
    filter_backends = [DjangoFilterBackend]
    filtersert = ['name','modele','desrcition','id_cathegorie__name','id_marque__name']

