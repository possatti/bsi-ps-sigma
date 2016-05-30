from django.db import models

class ProjetoDAO(models.Manager):
    def util_instanciar_projeto(self, linha):
        projeto = self.model(
            id=linha[0],
            nome=linha[1],
            descricao=linha[2],
            inicio=linha[3],
            fim=linha[4],
            progresso=linha[5],
            linkGithub=linha[6],
            linkGoogleDrive=linha[7],
            linkSlack=linha[8],
            linkTaiga=linha[9],
            fase=linha[10],
            metodologia=linha[11],
            prioridade=linha[12],
            situacao=linha[13])
        return projeto

    def inserir(self, projeto):
        projeto.save()

    def excluir(self, projeto):
        projeto.delete()

    def alterar(self, projeto):
        projeto.save()

    def consultar(self, id_projeto):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT *
            FROM gestaoprojetos_projeto p
            WHERE p.id = """ + str(id_projeto))
        linha = cursor.fetchall()[0]
        projeto = self.util_instanciar_projeto(linha)
        return projeto


    def consultarTodos(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT *
            FROM gestaoprojetos_projeto p
        """)
        projetos = []
        for linha in cursor.fetchall():
            projeto = self.util_instanciar_projeto(linha)
            projetos.append(projeto)
        return projetos

#    def consultarTodosDeUmaEE(self, entidade_externa):
#        pass

    def consultarPorPrioridade(self, prioridade):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT *
            FROM gestaoprojetos_projeto p
            WHERE p.prioridade = """ + '"' + prioridade + '"')
        projetos = []
        for linha in cursor.fetchall():
            projeto = self.util_instanciar_projeto(linha)
            projetos.append(projeto)
        return projetos
