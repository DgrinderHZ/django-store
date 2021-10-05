from rest_framework.serializers import ModelSerializer


from categories.models import Category
from products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'brand', 'price', 'description', 'category']


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
