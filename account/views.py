from django.shortcuts import render
from django.http import JsonResponse

from .serializer import *
from.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db import IntegrityError
from rest_framework import generics,viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
#classe permetant de creer un client
# class MultileSerializersUser:

#     def get_serialier_class(self,request):
#         if request
    

class TestREgister(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


    def create(self, request, *args, **kwargs):
        print(request.data)

        
        user = Client.objects.create_user(
            username=request.data['username'],
            password=request.data['password'],
            email=request.data['email'],

        )
        # user = dict(user)
        if user is not None :
        # user = dict(user)
            return Response('user cant not register ',status=status.HTTP_400_BAD_REQUEST)
        return Response('succes register user',status=status.HTTP_200_OK)
        
             

class MarchantREgister(viewsets.ModelViewSet):
    serializer_class = MarchantSerializer
    queryset = Marchand.objects.all()
    def create(self, request, *args, **kwargs):
        print(request.data)  
        is_staff = request.data.get('is_staff', True)
        user = Marchand.objects.create_user(
            username=request.data['username'],
            password=request.data['password'],
            email=request.data['email'],
            is_staff = is_staff
        )
        # user = dict(user)
        if user is not None :

            
        # user = dict(user)
            return Response('user cant not register ',status=status.HTTP_400_BAD_REQUEST)
        return Response('succes register user',status=status.HTTP_200_OK)
        
             

class AdminREgister(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    def create(self, request, *args, **kwargs):
        print(request.data)
        user = Admin.objects.create_superuser(
            username=request.data['username'],
            password=request.data['password'],
            email=request.data['email'],

        )
        if user is not None :

            
        # user = dict(user)
            return Response('user cant not register ',status=status.HTTP_400_BAD_REQUEST)
        return Response('succes register user',status=status.HTTP_200_OK)
        
                    



class ClientRegister(generics.CreateAPIView):
    authentication_classes=[
        BasicAuthentication
    ]
    serializer_class =ClientSerializer
    permission_classes =[AllowAny]
    def post(self, request,*args, **kwargs):
        if not request.data:
            return Response(
                 {"error": "Please provide the required fields"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')

        try:
            if (username 
            and Client.objects.exclude(username__isnull=True)
            .exclude(username__exact="")
            .filter(username = username)
            .exists()
            ):
                return Response(
                    {"error": "This username is already taken"},
                    status=status.HTTP_402_BAD_REQUEST,
                )
            if(
                email
                and
                Client.objects.exclude(email__isnull=True)
                .exclude(email__exact="")
                .filter(email=email.lower())
                .exists()

            ):
                return Response(
                    {
                        "`erros":"User with this email already exists"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except IntegrityError:
            return Response(
                {"error": "Integrity error"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user=serializer.save(is_active=True)
        user.save()

        return Response(
            {
                "success":"User registered successfully"
            },
             status=status.HTTP_201_CREATED,
        )



class ClientLogin(generics.GenericAPIView):
    serializer_class=UserLoginSerializer

    permission_classes=[AllowAny]
    def post(self, request, *args, **kwargs):
            # print(request.data)
            username = request.data['username'
                                        ]
            password = request.data['password']

            user = Client.objects.filter(username=username).first()
            if not user:
                user =Marchand.objects.filter(username=username).first()
                if not user:
                    user =Admin.objects.filter(username=username).first()
                    if not user:
                        raise AuthenticationFailed('user not found') 
            if user.check_password(password):
                if not user.is_active:
                    raise ValueError("User account is not active")
                # if not user.phone_number_verified and email_or_phone.startswith("+"):
                #     raise ValueError("Phone number not verified")

            serializer = self.get_serializer(data=request.data)

            # serializer.is_valid(raise_exception=True)

            serializer.is_valid(raise_exception=True)
            errors = serializer.errors

            for field, error_msgs in errors.items():
                print(f"Field: {field}")
                for msg in error_msgs:
                    print(f"Error: {msg}")
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)



    # def post(self, request):
    #     usernme = request.data['username']
    #     password = request.data['password']

    #     user = Client.objects.filter(usernme=usernme).first()

    #     if user.check_password(password):
    #         if not user.is_active:
    #             raise ValueError("User is not activate")
            
    #     if not user:
    #         raise AuthenticationFailed('user not found ')
        
    #     serializer = self.get_serializer(data=request.data)

    #     serializer.is_valid(raise_exception=True)
    #     erros = serializer.erros

    #     for field ,err_msg in erros.items():
    #         print(f"Field:{field}")
    #         for msd in err_msg:
    #             print(f"errors:{msd}")
    #     refresh = RefreshToken.for_user(user)

    #     return Response(
    #         {
    #             'refresh':str(refresh),
    #             'access':str(refresh.access_token)
    #         },status=status.HTTP_200_OK
    #     )

