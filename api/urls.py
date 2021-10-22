from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from .views import CategoryViewSet, ProductViewSet, UserCreate, UserLoginView


schema_view = get_swagger_view(title="Store API")
urlpatterns = [
    path('api/users/', UserCreate.as_view(), name='user_create'),
    path('api/login/', UserLoginView.as_view(), name='user_login'),
    path(r'api/docs/', schema_view, name='api'),
]

# ViewSets
router = DefaultRouter()
router.register('api/category', CategoryViewSet, basename='category')
router.register('api/product', ProductViewSet, basename='product')
urlpatterns += router.urls
