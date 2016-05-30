from gestaoProjetos.DAOs.ProjetoDAO import ProjetoDAO

def novoProjeto(projeto):
    ProjetoDAO.inserir(projeto)

def alterarProjeto(projeto):
    ProjetoDAO.alterar(projeto)

def excluirProjeto(projeto):
    ProjetoDAO.excluir(projeto)

# def alocarParticipante(participante, projeto):
#     pass

# def novaTecnologia():
#     pass

# def AlterarTecnologia():
#     pass

# def excluirTecnologia():
#     pass
