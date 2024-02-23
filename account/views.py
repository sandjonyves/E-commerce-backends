from django.shortcuts import render
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db import IntegrityError
from rest_framework import generics,viewsets
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from rest_framework import status
#classe permetant de creer un client

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
        return Response(JsonResponse(request.data,safe=False)
                        ,status= status.HTTP_200_OK)

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
            if user.check_password(password):
                if not user.is_active:
                    raise ValueError("User account is not active")
                # if not user.phone_number_verified and email_or_phone.startswith("+"):
                #     raise ValueError("Phone number not verified")

            if not user:
                raise AuthenticationFailed('user not found')       
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

