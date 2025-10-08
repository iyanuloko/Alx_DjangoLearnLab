from rest_framework import serializers
from .models import User

class SignUpFormSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def validate(self, data):
            if len(data['password']) < 8:
                raise serializers.ValidationError('Password must be at least 8 characters')

class ProfileViewSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_pic', 'bio']