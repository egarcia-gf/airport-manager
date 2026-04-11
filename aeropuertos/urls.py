from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('favoritos/', views.lista_favoritos, name='lista_favoritos'),
    path('favoritos/agregar/', views.agregar_favorito, name='agregar_favorito'),
    path('favoritos/eliminar/<int:favorito_id>/', views.eliminar_favorito, name='eliminar_favorito'),
    path('distancia/', views.calcular_distancia, name='calcular_distancia'),
    path('comparar/', views.comparar_aeropuertos, name='comparar_aeropuertos'),
    path('pais/', views.buscar_por_pais, name='buscar_por_pais'),
]