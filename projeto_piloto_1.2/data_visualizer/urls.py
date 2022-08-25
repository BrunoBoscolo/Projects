from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dados/', views.dados, name='dados'),
    path('dados/paciente/<pacient>', views.dados_pacient, name='dados_pacient'),
    path('insertar/', views.insertar, name='insertar'),
    path('consulta/', views.consulta, name='consulta'),
    path('confirmation/<name>', views.confirmation, name='confirmation'),
]