from Pasta_Poli import Insersor, Repositorio

repo = Repositorio()
insersor = Insersor(repo)

data = insersor.inserir_dado('Edson', 39)
print(data)
