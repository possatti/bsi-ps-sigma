from django.db import models
from .DAOs.ProjetoDAO import ProjetoDAO

class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    inicio  = models.DateTimeField(auto_now_add=False)
    fim = models.DateTimeField(auto_now_add=False)
    progresso = models.FloatField()
    linkGithub = models.URLField(blank=True)
    linkGoogleDrive = models.URLField(blank=True)
    linkSlack = models.URLField(blank=True)
    linkTaiga = models.URLField(blank=True)

    # Enums
    SITUACAO_CHOICES = [('P', 'Pendente'), ('E', 'Em andamento'), ('F', 'Finalizado')]
    FASE_CHOICES = [('I', 'Inception'), ('C', 'Concepção'), ('D', 'Desenvolvimento'), ('M', 'Implantação'), ('T', 'TLE')]
    PRIORIDADE_CHOICES = [('B', 'Baixa'), ('M', 'Média'), ('A', 'Alta')]
    METODOLOGIA_CHOICES = [('C', 'Cascata'), ('I', 'Iterativo'), ('A', 'Agil'), ('E', 'Evolutivo')]
    situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES, default='P')
    fase = models.CharField(max_length=1, choices=FASE_CHOICES, default='I')
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES, default='B')
    metodologia = models.CharField(max_length=1, choices=METODOLOGIA_CHOICES, default='C')

    # Relacionamentos
    # cliente = models.ForeignKey('gestaoProjetos.EntidadeExterna', models.CASCADE)

    objects = ProjetoDAO()

    def __str__(self):
      return self.nome
