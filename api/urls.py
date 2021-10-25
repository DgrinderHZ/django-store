from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, UserCreate, UserLoginView


# drf-yasg API docs
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('api/users/', UserCreate.as_view(), name='user_create'),
    path('api/login/', UserLoginView.as_view(), name='user_login'),

    # drf-yasg 
    url(r'^api/swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
        ),
    url(r'^api/swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
        ),
    url(r'^api/redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
        ),
]

# ViewSets
router = DefaultRouter()
router.register('api/category', CategoryViewSet, basename='category')
router.register('api/product', ProductViewSet, basename='product')
urlpatterns += router.urls
