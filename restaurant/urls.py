# # from django.urls import path

# app_name = 'restaurant'

# urlpatterns = [
# ]

# restaurant/urls.py
from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('show-json-restaurant/', views.show_json_restaurant, name='show_json_restaurant'),
]