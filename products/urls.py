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
"""

from django.urls import path

from products.views import products_list, ProductDetailView
from products.views import ProductCreateView, ProductUpdateView, product_delete

urlpatterns = [
    path('products/', products_list, name='products_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete')
]
