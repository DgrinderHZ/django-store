from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

from categories.models import Category
from products.models import Product


User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'brand', 'price', 'description', 'category']


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
