from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

urlpatterns = [
]

# ViewSets
router = DefaultRouter()
router.register('api/category', CategoryViewSet, basename='category')
urlpatterns += router.urls
