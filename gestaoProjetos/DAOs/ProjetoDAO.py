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
        pass

    def excluir(self, projeto):
        pass

    def alterar(self, projeto):
        pass

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
            projetos.append(projeto)
        return projetos

    def consultarTodosDeUmaEE(self, entidade_externa):
        pass

    def consultarPorPrioridade(self, prioridade):
        pass


class PollManager(models.Manager):
    def with_counts(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT p.id, p.question, p.poll_date, COUNT(*)
            FROM polls_opinionpoll p, polls_response r
            WHERE p.id = r.poll_id
            GROUP BY p.id, p.question, p.poll_date
            ORDER BY p.poll_date DESC""")
        result_list = []
        for row in cursor.fetchall():
            p = self.model(id=row[0], question=row[1], poll_date=row[2])
            p.num_responses = row[3]
            result_list.append(p)
        return result_list
