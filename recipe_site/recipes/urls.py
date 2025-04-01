from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('recipe/edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('accounts/register/', views.register, name='register'),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('recipe/edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
]