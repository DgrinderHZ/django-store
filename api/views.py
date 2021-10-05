from rest_framework.viewsets import ModelViewSet
from api.serializers import CategorySerializer, ProductSerializer

from categories.models import Category
from products.models import Product


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
