from rest_framework.viewsets import ModelViewSet
from api.serializers import CategorySerializer

from categories.models import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer