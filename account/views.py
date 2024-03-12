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
#classe permetant de creer un client
# class MultileSerializersUser:

#     def get_serialier_class(self,request):
#         if request
    

class ClientRegister(viewsets.ModelViewSet):
  
    serializer_class = ClientSerializer
    queryset = CustomUser.objects.all()
    #definition des permissions 
    permission_classes = [AllowAny]
    def create(self, request, *args, **kwargs):
        
        data = request.data
       
        user_type = data.get('user_type')
        # is_staff = data.get('is_staff',True)
        # is_superuser = data.get('is_superuser',True)
        # user_type = data.pop('user_type')
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)


        if int(user_type) == 1:
            user = CustomUser.objects.create_superuser(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            email=serializer.validated_data['email'],   
        )
            if user is None:
                raise('user can not creer', status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            try :
                Admin.objects.create(user=user)
            except:
                data = CustomUser.objects.get(username=user.username)
                data.delete()
                raise('user can not creer', status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        elif int(user_type) == 2:  
            user = CustomUser.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            email=serializer.validated_data['email'], 
            is_staff = True  
        )
            if user is None:
                raise('user can not creer', status.HTTP_500_INTERNAL_SERVER_ERROR)     
            try :
                Marchand.objects.create(user=user)
            except:
                data = CustomUser.objects.get(username=user.username)
                data.delete()
                raise('user can not creer', status.HTTP_500_INTERNAL_SERVER_ERROR)      
               
        else:  
            user = CustomUser.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            email=serializer.validated_data['email'], 

        )
            if user is None:
                raise('user can not creer', status.HTTP_500_INTERNAL_SERVER_ERROR)        
            try :
              Client.objects.create(
            user=user, 
            )
            except:
                data = CustomUser.objects.get(username=user.username)
                data.delete()
                
                raise('user can not creer', status.HTTP_500_INTERNAL_SERVER_ERROR)
            

        return Response('succes register user',status=status.HTTP_200_OK)
          
             

class ReadOnlyUser(APIView):


    # @action(detail=False,methods=['post'],)
    def get(self,request,user_type):
        queryset ={}
        if int(user_type) == 1:
            queryset = Admin.objects.all()
        elif int(user_type==2):
            queryset = Marchand.objects.all()
        else:
            queryset = Client.objects.all()
        print(queryset)
        data = list(queryset.values('user__username','user__email','user__password'))

        return JsonResponse(data,safe=False,status=status.HTTP_200_OK)




class UserLogin(APIView):
    pass

    serializer_class=UserLoginSerializer
    
    permission_classes=[AllowAny]

    def post(self,request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
     
        if not user:
            raise serializers.ValidationError('data is not valid')
        if not user.is_active:
            raise serializers.ValidationError('user is not activated ')
       
        login(request,user)
        token = RefreshToken.for_user(user)
        # token['is_activate']=user.is_active
        # token['is_staff']=user.is_staff
        # token['is_superuser']=user.is_superuser

        return Response({
            'refresh': str(token),
            'access': str(token.access_token)
        }, status=status.HTTP_200_OK)

class Logout(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        print(request.user)
        logout(request)

        return Response({
          'message': 'logout succesfull'
        }, status=status.HTTP_200_OK)
    def get(self, request):
        print(request.user)
        if request.user.is_authenticated:
            # L'utilisateur est connecté
            return Response({'message': 'Utilisateur connecté'})
        else:
            # L'utilisateur n'est pas connecté
            return Response({'message': 'Utilisateur non connecté'})
