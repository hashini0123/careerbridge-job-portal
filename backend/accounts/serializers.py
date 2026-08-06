from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelsSerializer):
    class Meta:
        model = User
        field = ["id" , "username" , "email", "role"]
        extra_kwargs = {"password" : {"write_only" : True}}


class RegisterSerializer(serializers.ModelsSerializer):
    class Meta: 
        model = User
        field = ["id" , "username" , "password" , ""]
        extra_kwargs = {"password" : {"write_only" : True}}

def create(self,validated_data):
    user = User.objects.create_user(**validated_data)
    return user    