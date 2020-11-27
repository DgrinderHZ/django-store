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

from .views import add_to_cart, cart, remove_from_cart, clear_cart

urlpatterns = [
    path('carts/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('carts/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('carts/clear_cart/', clear_cart, name='clear_cart'),
    path('carts/cart/', cart, name='cart'),
]
