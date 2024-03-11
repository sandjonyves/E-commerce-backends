from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate,get_user_model,login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
# CustomUser = get_user_model()

#serializeur du client
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model =CustomUser
        fields = ('__all__')
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        client = Client.objects.create(user=user,role='client')

        return user


class MarchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marchand
        fields = ('__all__')


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
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
