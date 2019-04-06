from django.shortcuts import render
from django.views.generic import ListView

from .models import Chamado


class ChamadoView(ListView):
    model = Chamado
    template_name = 'app_helpdesk/chamado.html'

class ChamadoHomeView(ListView):
    model = Chamado
    template_name = 'app_helpdesk/home.html'

class ChamadoAtendidoView(ListView):
    model = Chamado
    template_name = 'app_helpdesk/atendidos.html'
