# adtv1.py
from adtv2 import AbstractClass
class Filha(AbstractClass):
    def apresentar_metodo(self) -> None:
        print(self.atributo)
    def metodo_abstrato(self) -> None: #4:
        print('Implementando método abstrato.')
filha = Filha()
filha.apresentar_metodo() #1:
filha.metodo('Estou aqui.') #2:
filha.metodo_abstrato() #5:
# Trecho c/ Error após usar @abstractmethod.
abstractclass = AbstractClass() #5:
abstractclass.metodo('Fazendo algo.') #3: #6:


#1: Resposta (s/ @abstractmethod em adtv2.py): Olá mundo.
#2: Resposta (s/ @abstractmethod em adtv2.py): Estou aqui.
#3: Resposta (s/ @abstractmethod em adtv2.py): Fazendo algo.
#4: Incluindo este método/função p/ conseguimos parte da resposta (#1, #2 e #2 funcionou, mas apresentou um último erro por cont ado #5:).
#5: Chamando o método_abstrato().
#6: Erro (c/ @abstractmethod em adtv2.py): TypeError: Can't instantiate abstract class AbstractClass with abstract method metodo_abstrato.
