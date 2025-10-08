from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class SignUpFormSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def validate(self, data):
            if len(data['password']) < 8:
                raise serializers.ValidationError('Password must be at least 8 characters')

        def create(self, validated_data):
            return get_user_model().objects.create_user(**validated_data)
            Token.objects.create(user=self)
            return user

class ProfileViewSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_pic', 'bio']