# coding: utf-8
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                attrs['user'] = user
                return attrs
            else:
                msg = 'Invalid Credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = "Invalid Parameters."
            raise serializers.ValidationError(msg)



class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
