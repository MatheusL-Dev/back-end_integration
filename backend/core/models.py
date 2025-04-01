from django.db import models


class Tarefa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Pendente')

    def __str__(self):
        return self.nome