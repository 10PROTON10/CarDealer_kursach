from catalog.models import Brand, Car, Customer, Order, Review, CarAccessory, Favorite
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = Customer.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=password
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = Customer.objects.filter(username=username).first()
            print(f"Validate: Username: {username}, Password: {password}, User: {user}")

            if user and user.check_password(password):
                return data
            raise serializers.ValidationError('Invalid username or password.')
        raise serializers.ValidationError('Must include "username" and "password."')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class FavoriteCarSerializer(serializers.ModelSerializer):
    car = CarSerializer()  # Используйте CarSerializer в качестве вложенного сериализатора

    class Meta:
        model = Favorite
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    def get_user(self, obj):
        user = obj.author
        return {
            'id': user.id,
            'username': user.username
        }

class CarAccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAccessory
        fields = '__all__'


