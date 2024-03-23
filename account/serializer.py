
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,get_user_model,login
from django.contrib.auth.models import Permission,Group

from rest_framework import serializers
from rest_framework import status

from .permissions import group_permissionOfcathegorie_piece 
from .models import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#serializeur du client
class UserSerializer(serializers.ModelSerializer):
    # user_type = serializers.IntegerField(write_only = True)
    def create(self, validated_data):
        """
        Create and save a new user with the given validated data.
        """
        role = validated_data.pop('role')
        password = validated_data.pop('password')

        if role == CustomUser.Role.ADMIN:
            user = Admin.objects.create(
                # The password must be hashed before saving it to the database.
                password=make_password(password),
                is_staff=True,
                is_superuser=True,
                **validated_data
            )
            if user is None:
                raise ValueError('Unable to create user.')

        elif role == CustomUser.Role.MARCHAND:
            user = Marchand.objects.create(
                password=make_password(password),
                is_staff=True,
                **validated_data
            )
            if user is None:
                raise ValueError('Unable to create user.')
            try:
                group = Group.objects.get(name='marchandGourpPermission')
            except Group.DoesNotExist:
                group = group_permissionOfcathegorie_piece()
            user.groups.add(group)

        else:
            user = Client.objects.create(
                password=make_password(password),
                **validated_data
            )
            if user is None:
                raise ValueError('Unable to create user.')

        return user

class MarchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marchand
        fields = ('__all__')


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('__all__')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')

class UserLoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()
    password = serializers.CharField()





    # def validate(self, request):
    #     print(request)
    #     username = request.get('username')
    #     password = request.get('password')

    #     user = authenticate(username=username, password=password)

    #     if not user:
    #         raise serializers.ValidationError('data is not valid')
    #     if not user.is_active:
    #         raise serializers.ValidationError('user is not activated ')
    #     login(request,user)
    #     token = self.get_token(user)
    #     token['is_activate']=user.is_active
    #     token['is_staff']=user.is_staff
    #     token['is_superuser']=user.is_superuser

    #     return {
    #         'refresh': str(token),
    #         'access': str(token.access_token),
    #     }
