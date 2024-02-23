from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets,response
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.decorators import api_view,action
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse


class PierceViewSet(viewsets.ModelViewSet):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer
    # @action(detail = False,methods=['get'],url_path = 'get_piece/(?P<id>\w+)')
    # def get_piece(self,request,id):
    #     queryset = Piece.objects.filter(id_cathegorie=id)
    #     data = list(queryset.values())
    #     return JsonResponse(data,safe=False)
       

class cathegorieViewSet(viewsets.ModelViewSet):
    queryset = Cathegorie.objects.all()
    serializer_class = CathegorieSerializer

    # @action(detail = False,methods=['get'],url_path = 'get_cathegorie/(?P<id>\w+)')
    # def get_cathegorie(self,request,id):
    #     queryset = Cathegorie.objects.filter(id_voiture=id)
    #     data = list(queryset.values())
    #     return JsonResponse(data,safe=False)
       




class TestView(generics.UpdateAPIView):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

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