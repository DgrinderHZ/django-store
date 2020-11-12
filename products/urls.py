"""products URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from products.views import products_list, products_details
from products.views import product_add, product_edit

urlpatterns = [
    path('products/', products_list, name='products_list'),
    path('products/<int:pk>', products_details, name='product_details'),
    path('products/add', product_add, name='product_add'),
    path('products/edit/<int:pk>', product_edit, name='product_edit')
]
