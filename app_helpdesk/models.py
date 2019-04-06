from django.db import models
from django.contrib.auth.models import User

class Categoria (models.Model):
    nomeCategoria = models.CharField('Categoria:', max_length=60)
    descricaoCategoria = models.CharField('Descrição da categoria:', max_length=60)

class Funcionario (models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE,
        verbose_name = 'Usuario')
    nome = models.CharField('Nome', max_length=60)
    departamento = models.CharField('Departamento', max_length=60)

class Atendimento (models.Model):
        laudoAtendimento = models.TextField('Descrição do atendimento:', max_length=60)
        Funcionario = models.ForeignKey(Funcionario, on_delete = models.CASCADE)
        def __str__(self):
            return self.laudoAtendimento

class Chamado (models.Model):
    titulo = models.CharField('Título:', max_length=60)
    Descricao = models.TextField('Título:')
    telefone = models.CharField('Telefone solicitante', max_length=60)
    departamento = models.ManyToManyField(Funcionario)
    data = models.DateTimeField('Data chamado')
    atendimento = models.ManyToManyField(Atendimento)
    categoria = models.ManyToManyField(Categoria)
    status = models.CharField('Status', max_length=60)