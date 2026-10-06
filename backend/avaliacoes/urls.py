from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_avaliacoes),
    path('pendentes/', views.listar_pendentes),
    path('resumo/', views.resumo),
]
