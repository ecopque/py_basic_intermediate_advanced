class Pessoa:
    def __init__(self, nome, cpf, altura):
        self.nome = nome
        self.cpf = cpf
        self.altura = altura
    def meu_metodo(self):
        pass
class Secretaria(Pessoa):
    def __init__(self, id_secretaria, nome, cpf, altura):
        super().__init__(nome, cpf, altura) #1: #2:
        self.id_secretaria = id_secretaria
class Vendedor(Pessoa):
    def __init__(self, total_vendas, nome, cpf, altura):
        super().__init__(nome, cpf, altura)
        total_vendas += 10 #4:
        self.total_vendas = total_vendas
    pass
s1 = Secretaria(2, 'Mel', 123456, 171) #3:
v1 = Vendedor(150.70, 'Théo', 987654, 173)
print(s1.id_secretaria) #5:
print(v1.total_vendas) #6:


#1: super() é o mesmo que classe-pai, ou seja, neste caso a classe "Pessoa"/__init__. Também poderíamos chamar qualquer método que existir na classe, ex: super().meu_metodo().
#2: Estamos enviando para a classe-pai/__init__ (Pessoa) os seguintes parâmetros: "nome", "cpf" e "altura".
#3: Agora temos que receber 4 parâmetros (em vez de 3, como antes).
#4: Estamos manipulando o valor de vendas (adicionando 10). Só de onda.
#5: Resposta: 2.
#6: Resposta: 160.7.