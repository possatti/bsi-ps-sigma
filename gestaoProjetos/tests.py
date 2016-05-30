from django.test import TestCase
from gestaoProjetos.models import Projeto

class ProjetoTest(TestCase):
    def setUp(self):
        Projeto.objects.create(
            nome="LifeBoxTest",
            inicio="2016-05-20 01:19:30",
            fim="2016-05-20 01:19:37",
            progresso=0,
            fase="I",
            metodologia="C",
            prioridade="B",
            situacao="P")

    def test_consultar_todos(self):
        projetos = Projeto.objects.all()
        self.assertEqual(len(projetos), 1)
        self.assertEqual(projetos[0].nome, "LifeBoxTest")

class ProjetoDAOTest(TestCase):
    def setUp(self):
        Projeto.objects.create(
            nome="LifeBoxTest",
            inicio="2016-05-20 01:19:30",
            fim="2016-05-20 01:19:37",
            progresso=0,
            fase="I",
            metodologia="C",
            prioridade="B",
            situacao="P")

    def test_consultar(self):
        projeto = Projeto.objects.consultar(1)
        self.assertEqual(projeto.nome, "LifeBoxTest")

    def test_consultarTodos(self):
        projetos = Projeto.objects.consultarTodos()
        self.assertEqual(len(projetos), 1)
        self.assertEqual(projetos[0].nome, "LifeBoxTest")
