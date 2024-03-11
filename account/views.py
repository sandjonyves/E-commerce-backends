from django.shortcuts import render
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate ,login,get_user_model
# CustomUser = get_user_model()
from .serializer import *
from.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser

from rest_framework import generics,viewsets
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
        print(request.data)
        user=CustomUser.objects.create_user(
            username=request.data['username'],
            password=request.data['password'],
            email=request.data['email'],
        )
        if user is not None :
        # user = dict(user)
            return Response('user cant not register ',status=status.HTTP_400_BAD_REQUEST)

        client = Client.objects.create(
            user = user,
            role='client'
           
        )
        
        # user = dict(user)
        if client is not None :
        # user = dict(user)
            return Response('user cant not register ',status=status.HTTP_400_BAD_REQUEST)
        return Response('succes register user',status=status.HTTP_200_OK)
        
             

class MarchantREgister(viewsets.ModelViewSet):
    authentication_classes = [authentication.JWTAuthentication] 

    permission_classes = [IsAdminUser]
    serializer_class = MarchantSerializer
    queryset = Marchand.objects.all()

    def create(self, request, *args, **kwargs):
        print(request.data)  
        is_staff = request.data.get('is_staff', True)
        user=CustomUser.objects.create_user(
            username=request.data['username'],
            password=request.data['password'],
            email=request.data['email'],
            is_staff = is_staff
        )
        if user is not None :
        # user = dict(user)
            return Response('user cant not register ',status=status.HTTP_400_BAD_REQUEST)

        marchand = Marchand.objects.create_user(
            user = user,
            role='marchand'
           
        )
        
        # user = dict(user)
        if marchand is not None :
        # user = dict(user)
            return Response('user cant not register ',status=status.HTTP_400_BAD_REQUEST)
        return Response('succes register user',status=status.HTTP_200_OK)
        
             

class AdminREgister(viewsets.ModelViewSet):

    permission_classes = [AllowAny]
    serializer_class = AdminSerializer
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = CustomUser.objects.create_superuser(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            email=serializer.validated_data['email']
        )

        admin = Admin.objects.create(user=user, role='admin')

        if admin is  None:
            return Response('Failed to register user.', status=status.HTTP_400_BAD_REQUEST)

        return Response('Successfully registered user.', status=status.HTTP_200_OK)
                    



# 

class UserLogin(APIView):

    serializer_class=UserLoginSerializer
    
    permission_classes=[AllowAny]

    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        # print(111111111111111111111111111111111111111111111111)
        # user = Client.objects.filter(username=username).first()
        # if not user:
        #     user =Marchand.objects.filter(username=username).first()
        #     if not user:
        #         user =Admin.objects.filter(username=username).first()
        #         if not user:
        #             raise AuthenticationFailed('user not found') 
        # if user.check_password(password):
        #     if not user.is_active:
        #         raise ValueError("User account is not active")
        # print(111111111111111111111111111111111111111111111111)
        user = authenticate(username=username, password=password)
        print(111111111111111111111111111111111111111111111113)
        if not user:
            raise serializers.ValidationError('data is not valid')
        if not user.is_active:
            raise serializers.ValidationError('user is not activated ')
        print(111111111111111111111111111111111111111111111111)
        # login(request,user)
        token = RefreshToken.for_user(user)
        # token['is_activate']=user.is_active
        # token['is_staff']=user.is_staff
        # token['is_superuser']=user.is_superuser

        return Response({
            'refresh': str(token),
            'access': str(token.access_token)
        }, status=status.HTTP_200_OK)


    # def post(self, request, *args, **kwargs):
    #         # print(request.data)
    #         username = request.data['username']
    #         password = request.data['password']
    #         # user = Client.objects.filter(username=username).first()
    #         # if not user:
    #         #     user =Marchand.objects.filter(username=username).first()
    #         #     if not user:
    #         #         user =Admin.objects.filter(username=username).first()
    #         #         if not user:
    #         #             raise AuthenticationFailed('user not found') 
    #         # if user.check_password(password):
    #         #     if not user.is_active:
    #         #         raise ValueError("User account is not active")
    #         user = authenticate(
    #         username=request.data["username"],
    #         password=request.data["password"]
    #         )

    #         if not user:
    #             raise serializers.ValidationError("Identifiants invalides")

    #         if not user.is_active:
    #             raise serializers.ValidationError("Votre compte est désactivé")

    #         # Générez le token JWT
    #         # login(request,user)
    #         refresh = self.get_token(user)

    #         # Ajoutez des données supplémentaires au token si nécessaire
    #         refresh['username'] = user.username
    #         # ...

    #         return {
    #             'refresh': str(refresh),
    #             'access': str(refresh.access_token),
    #         }

                # if not user.phone_number_verified and email_or_phone.startswith("+"):
                #     raise ValueError("Phone number not verified")
            # serializer = self.get_serializer(data=request.data)
            # # serializer.is_valid(raise_exception=True)
            # serializer.is_valid(raise_exception=True)
            # errors = serializer.errors
            # for field, error_msgs in errors.items():
            #     print(f"Field: {field}")
            #     for msg in error_msgs:
            #         print(f"Error: {msg}")
            # refresh = RefreshToken.for_user(user)

            # return Response({
            #     'refresh': str(refresh),
            #     'access': str(refresh.access_token)
            # }, status=status.HTTP_200_OK)

            
    # def validate(self, attrs):
    #     # Effectuez ici vos validations personnalisées
    #     # Par exemple, vérifiez si l'utilisateur est actif ou si les informations d'identification sont valides

    #     # Récupérez l'utilisateur
    #     user = authenticate(
    #         username=attrs.get("username"),
    #         password=attrs.get("password")
    #     )

    #     if not user:
    #         raise serializers.ValidationError("Identifiants invalides")

    #     if not user.is_active:
    #         raise serializers.ValidationError("Votre compte est désactivé")

    #     # Générez le token JWT
    #     refresh = self.get_token(user)

    #     # Ajoutez des données supplémentaires au token si nécessaire
    #     refresh['username'] = user.username
    #     # ...

    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token),
    #     }


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



# class ClientRegister(generics.CreateAPIView):
#     authentication_classes=[
#         BasicAuthentication
#     ]
#     serializer_class =ClientSerializer
#     permission_classes =[AllowAny]
#     def post(self, request,*args, **kwargs):
#         if not request.data:
#             return Response(
#                  {"error": "Please provide the required fields"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         serializer = self.get_serializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         username = serializer.validated_data.get('username')
#         email = serializer.validated_data.get('email')

#         try:
#             if (username 
#             and Client.objects.exclude(username__isnull=True)
#             .exclude(username__exact="")
#             .filter(username = username)
#             .exists()
#             ):
#                 return Response(
#                     {"error": "This username is already taken"},
#                     status=status.HTTP_402_BAD_REQUEST,
#                 )
#             if(
#                 email
#                 and
#                 Client.objects.exclude(email__isnull=True)
#                 .exclude(email__exact="")
#                 .filter(email=email.lower())
#                 .exists()

#             ):
#                 return Response(
#                     {
#                         "`erros":"User with this email already exists"
#                     },
#                     status=status.HTTP_400_BAD_REQUEST
#                 )
#         except IntegrityError:
#             return Response(
#                 {"error": "Integrity error"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         user=serializer.save(is_active=True)
#         user.save()

#         return Response(
#             {
#                 "success":"User registered successfully"
#             },
#              status=status.HTTP_201_CREATED,
#         )