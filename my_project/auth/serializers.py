from rest_framework import serializers
from catalog.models import Customer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer  # Замените User на вашу модель Customer
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=128, write_only=True)