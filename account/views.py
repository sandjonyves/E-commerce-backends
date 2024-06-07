from django.db import transaction
from django.shortcuts import render
from django.contrib.auth import authenticate ,login,logout
from django.core.mail import send_mail

from .serializer import *
from.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework.decorators import action
from rest_framework import generics,viewsets,mixins
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from app.serializer import *
#classe permetant de creer un client
# class MultileSerializersUser:

#     def get_serialier_class(self,request):
#         if request
class PersonnalModelViewSet(
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass


 #fonction de creation d'adminintrateur
def createAdmin(validated_data):
    return Admin.objects.create(
        is_superuser = True,
        is_staff = True,
        **validated_data
    )
#fonction de creation d'un marchand
def createMarchand(validated_data):
    marchand= Marchand.objects.create(
        is_staff = True,
        **validated_data
    )
    #get the group permission of marchand
    # if is none I create a 0new group and add in this marchand
    try:
        group = Group.objects.get(name='marchandGourpPermission')
    except Group.DoesNotExist:
        group = group_permissionOfcathegorie_piece()
    marchand.groups.add(group)
    return Marchand

#fontion de creation d'un client 
def createClient(validated_data):
    return Client.objects.create(
        **validated_data
    )





class UserRegister(viewsets.ModelViewSet):

    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        #verify if the data request is good 
        print(request.data)
        if serializers.is_valid():
        
            role = serializers.validated_data.get('role')
            password = serializers.validated_data.get('password')
            email = serializers.validated_data.get('email')
            #hach the passeword of user 
            serializers.validated_data['password']  =  make_password(password)

            #create the user 
            if role == Admin.Role.ADMIN:
                user = createAdmin(serializers.validated_data)
            elif role == Marchand.Role.MARCHAND:
                user = createMarchand(serializers.validated_data)
            else:
                user = createClient(serializers.validated_data)
            #verifiction if the user have be succesfuli create
            if user is  None:
                return Response({'message':'error this user can not create '},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            #return status to 201 if the user have be create succesfuli    

            user = authenticate(email = email, password=password)
            if not user:
                raise serializers.ValidationError('data is not valid')
            if not user.is_active:
                raise serializers.ValidationError('user is not activated ')

            login(request, user)
            token = RefreshToken.for_user(user)
            # level_data = LevelSerializer(user.level_id).data if user.level_id else None
            # sector_data = SectorSerializer(user.sector_id).data if user.sector_id else None
            
            token['role'] = user.role
            token['firstName'] = user.firstName
            token['lastName']  = user.lastName
            token['email']  = user.email
            token['phone_number'] = user.phone_number
            token['password'] = user.password

            response_data = {
                'id':user.id,
                'refresh': str(token),
                'access': str(token.access_token),
                'message':'user create succesfuly'

            }
            return Response(response_data, status=status.HTTP_200_OK)
        
        else:
            return Response({"message":"data is not valid "},status=status.HTTP_400_BAD_REQUEST)


class MarchandUser(PersonnalModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = MarchandSerializer
    queryset = Marchand.objects.all()

class AdminUser(PersonnalModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = AdminSerializer
    queryset = Admin.objects.all()

#operation in the client 
class ClientUser(
                 PersonnalModelViewSet
    ):
    permission_classes = [AllowAny]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

   

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
        email = request.data['email']
        password = request.data['password']

        user = authenticate(email = email, password=password)

        if not user:
            return Response({"message":"data is not valid"},status=status.HTTP_400_BAD_REQUEST)
        if not user.is_active:
            return Response({"message":"User is not activate"},status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        
        token = RefreshToken.for_user(user)
        # level_data = LevelSerializer(user.level_id).data if user.level_id else None
        # sector_data = SectorSerializer(user.sector_id).data if user.sector_id else None
        token['role'] = user.role
        token['firstName'] = user.firstName
        token['lastName']  = user.lastName
        token['email']  = user.email
        token['phone_number'] = user.phone_number
        token['password'] = user.password


        response_data = {
            'id':user.id,
            'refresh': str(token),
            'access': str(token.access_token),
             'message':'user login succesfuly'
        }
        return Response(response_data, status=status.HTTP_200_OK)
      
        
# class Logout(APIView):
#     permission_classes=[AllowAny]
class Logout(APIView):
    permission_classes=[AllowAny]
    def post(self, request,id):
        user =  CustomUser.objects.filter(id=id).first
        request.user = user
        # print(request.user)
        logout(request)
        if not request.user.is_authenticated:

            return Response({
            'message': 'logout succesfull'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
            'message': 'logout failed'
            })
  
# fonction d'envoi des email

class SendMail(APIView):

    permission_classes =[AllowAny]
    def post(self,request):
        subjet = "constact de l'application de e-commerce"
        message = request.data.get('message')
        receive_mail= request.data.get('email')
        name = request.data.get('fullName')
        message = f'{name}\n\n {message}'

        send_mail(subjet,message,'sandjonyves@gmail.com',(receive_mail,))

        return Response({'message':'le message a ete envoyer avec succes '})


