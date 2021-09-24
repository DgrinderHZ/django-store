from django.urls import path
from .views import category_add, category_edit, category_list

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('categories/add/', category_add, name='category_add'),
    path('categories/edit/<int:pk>/', category_edit, name='category_edit'),
    #path('categories/delete/<int:pk>/', category_delete, name='category_delete')
]
