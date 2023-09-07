class Usuario:
    cargo = 'Usuário'
    def __init__(self, nome, idade, altura):
        self.altura = altura
    @staticmethod #1: #4: #5:
    def eh_adulto(idade): #2:
        if idade >= 18:
            print(True)
        else:
            print(False)
Usuario.eh_adulto(19) #3:


#1: Qual a principal diferença do @staticmethod para o @classmethod? Static não tem referência da própria classe (não sabe de qual classe está sendo chamado), ou seja, significa que ele não tem acesso aos atributos de classe (ex: cargo = 'Usuário'), não podendo ver ou modificar.
#2: Nesse método não recebo nem "cls" ou "self", porque ele não é um método de classe (p/ ter acesso aos atributos de classe), nem um método de instância (para ter acesso aos atributos de instância). Ele é um método estático.
#3: Resposta: True.
#4: Basicamente temos uma função normal só que dentro da classe. Mas se eu tentar acessar "cargo" (print(self.altura)) não vau funcionar.
#5: O método static é mais utilizado como método auxiliar. Pode utilizar desde que nunca vai precisar atributos de classe e nem vai precisar chamar uma função de instância ou atributos de instância (ou função/método de classe).
