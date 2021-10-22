from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.serializers import CategorySerializer,\
     ProductSerializer, UserSerializer

from categories.models import Category
from products.models import Product


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class UserLoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        un = request.data.get('username')
        pw = request.data.get('password')
        user = authenticate(username=un, password=pw)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response(
                {"error": "Wrong Credentials"},
                status=status.HTTP_400_BAD_REQUEST
            )


class CategoryViewSet(ModelViewSet):
    """
    Class based view, viewset Based:
    - List all code categories,
    - Create,
    - Retrieve,
    - Update or
    - Delete a category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProductViewSet(ModelViewSet):
    """
    Class based view, viewset Based:
    - List all code products,
    - Create,
    - Retrieve,
    - Update or
    - Delete a product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
