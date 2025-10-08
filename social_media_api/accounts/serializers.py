from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token

class SignUpFormSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def validate(self, data):
            if len(data['password']) < 8:
                raise serializers.ValidationError('Password must be at least 8 characters')

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)
        
class ProfileViewSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_pic', 'bio']