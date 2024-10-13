class Carrinho:
    def __init__(self):
        self._produtos = []
    def total(self):
        return sum([p.preco for p in self._produtos]) #1: #2:
    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nomeacao, produto.precificacao)
class Produto:
    def __init__(self, nome, preco):
        self.nomeacao = nome
        self.precificacao = preco
carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos() #3:
print(carrinho.total) #4:
