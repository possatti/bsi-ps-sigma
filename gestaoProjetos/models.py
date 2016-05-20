from django.db import models

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
    # cliente = models.ForeignKey('gestaoProjetos.EntidadeExterna', models.CASCADE)

    def __str__(self):
      return self.nome
