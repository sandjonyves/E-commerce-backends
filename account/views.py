from django.db import transaction
from django.shortcuts import render
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate ,login,get_user_model,logout

# CustomUser = get_user_model()
from .serializer import *
from.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework.decorators import action
from rest_framework import generics,viewsets,mixins
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt import authentication
from rest_framework.authentication import TokenAuthentication
from app.serializer import *
#classe permetant de creer un client
# class MultileSerializersUser:

#     def get_serialier_class(self,request):
#         if request
    

class UserRegister(viewsets.ModelViewSet):
    
    # def post(self, request):
    #     serializer =  UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    #definition des permissions 
  


  

class ReadOnlyUser(generics.RetrieveAPIView):
    serializer_class = AdminSerializer
    queryset =Admin.objects.all()

class readClient(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def get_queryset(self, request):
        """
        Return a filtered queryset based on the value of the `id` query parameter.
        """
        queryset = super().get_queryset()
        user_id = request.query_params.get("id")
        if user_id:
            queryset = queryset.filter(id=user_id)
        return queryset


class UserLogin(APIView):
    serializer_class=UserLoginSerializer
    
    permission_classes=[AllowAny]

    def post(self, request):
        """
        Login a user with their username and password.

        Parameters:
        username (str): The username of the user.
        password (str): The password of the user.

        Returns:
        Response: A JSON response containing the access and refresh tokens.

        Raises:
        ValidationError: If the provided credentials are invalid.
        """
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('data is not valid')
        if not user.is_active:
            raise serializers.ValidationError('user is not activated ')

        login(request, user)
        token = RefreshToken.for_user(user)
        # level_data = LevelSerializer(user.level_id).data if user.level_id else None
        # sector_data = SectorSerializer(user.sector_id).data if user.sector_id else None

        response_data = {
            'refresh': str(token),
            'access': str(token.access_token),
            'is_active': user.is_active,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            # 'level_id': level_data,
            # 'sector_id': sector_data
        }

        return Response(response_data, status=status.HTTP_200_OK)
        
class Logout(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        """
        Logs out the currently authenticated user.

        Parameters:
            request (HttpRequest): The incoming request.

        Returns:
            Response: A JSON response with a message indicating that the user was successfully logged out.
        """
        print(request.user)
        logout(request)

        return Response({
            'message': 'logout succesfull'
        }, status=status.HTTP_200_OK)
    # def get(self, request):
    #     print(request.user)
    #     if request.user.is_authenticated:
    #         # L'utilisateur est connecté
    #         return Response({'message': 'Utilisateur connecté'})
    #     else:
    #         # L'utilisateur n'est pas connecté
    #         return Response({'message': 'Utilisateur non connecté'})




# class RelatedReadUser(viewsets.ViewSet):
#     @action(detail=False,methods=["get"],url_path='sector-read/(?P<id_user>w+)')  
#     def sector_read(self,request, id_user):
#         queryset = Sector.objects.filter(user=id_user)
#         data = list(queryset.value())

#         return JsonResponse({'data':data,'status':status.HTTP_200_OK},safe=False,)

