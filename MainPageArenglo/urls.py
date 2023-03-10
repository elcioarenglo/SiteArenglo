
from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name= 'home'),
    path('perfil/', views.perfil, name= 'perfil'),
    path('contato/', views.contato, name= 'contato'),
    path('arquitetura/', views.arquitetura, name= 'arquitetura'),
    path('interiores/', views.interiores, name= 'interiores'),
    path('estrutura/', views.estrutura, name= 'estrutura'),
    path('hidreletrica/', views.hidreletrica, name= 'hidreletrica'),
    path('planejamento/', views.planejamento, name= 'planejamento'),
]

