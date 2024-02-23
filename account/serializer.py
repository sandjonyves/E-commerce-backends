from rest_framework import serializers
from .models import Client,Marchand,Admin
from django.contrib.auth import authenticate,get_user_model


#serializeur du client
class ClientSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Client
        fields = ('__all__')

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Unable to authenticate with provided credentials.')

        attrs['user'] = user
        return attrs
