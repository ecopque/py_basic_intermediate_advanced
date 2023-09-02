# adtv2.py
from abc import ABC, abstractmethod #1:
class AbstractClass(ABC): #2:
    def __init__(self):
        self.atributo = 'Olá mundo.'
    def metodo(self, elemento: str) -> None:
        print(elemento)
    @abstractmethod #3: #4: #5:
    def metodo_abstrato(self) -> None:
        pass



#1: O ABC é um objeto em que tudo que tivermos de elementos abstratos está presente nele. Então quando quisermos fazer uma classe abstrata temos que colocar a herança (ver #2:).
#2: Herança ABC (herdando percepção da idéia abstrata e elementos).
#3: Para python ter uma classe abstrata tem que necessariamente ter no mínimo um método abstrato.
#4: Transformamos este método abstrato (e por isso deu erro no código).
#5: Portanto, quando você adiciona @abstractmethod a um método, não é possível chamá-lo diretamente na classe base, mas você deve implementá-lo em todas as subclasses que herdam dessa classe base. A chamada ao método ocorrerá nas instâncias das subclasses, não na classe base. Não podemos acessá-la diretamente.
