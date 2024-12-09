from django.urls import path
from api import views

urlpatterns = [
    path('sort/<str:algorithm>/', views.sort_array, name='sort'),
]
