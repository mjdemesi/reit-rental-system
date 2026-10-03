from django.urls import path
from . import views

urlpatterns = [
    path('', views.unit_list, name='unit_list'),
    path('about/', views.about_reit, name='about_reit'),
]