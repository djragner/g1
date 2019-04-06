from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChamadoHomeView.as_view(), name = 'Chamado Principal'),
    path('chamados/', views.ChamadoView.as_view(), name = 'Chamados em aberto'),
    path('chamados/atendidos/', views.ChamadoAtendidoView.as_view(), name = 'Chamados em aberto'),
]