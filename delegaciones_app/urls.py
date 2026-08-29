from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('delegacion/<str:nombre>/', views.delegacion_detalle, name='delegacion_detalle'),
]
