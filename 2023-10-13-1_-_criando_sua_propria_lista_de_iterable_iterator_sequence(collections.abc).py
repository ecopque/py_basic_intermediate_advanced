from collections.abc import Sequence
class MyList(Sequence):
    def __init__(self):
        self._data = {} #1:
        self._index = 0
        self._next_index = 0 #8:
    def append(self, value):
        self._data[self._index] = value
        self._index += 1
    def __len__(self) -> int: #2:
        return self._index
    def __getitem__(self, index): #3:
        print('getitem:', index)
        return self._data[index]
    def __setitem__(self, index, value): #13:
        self._data[index] = value
    def __iter__(self): #6:
        return self
    def __next__(self): #7:
        if self._next_index >= self._index: #10:
            raise StopIteration
        value = self._data[self._next_index] #9:
        self._next_index += 1
        return value
if __name__ == '__main__':
    lista = MyList()
    lista.append('Hipácia')
    lista[0] = 'Edson' #12: #14:
    lista.append('Dienekes')
    print(lista[0]) #4: #15:
    print(len(lista)) #5:
    for item in lista:
        print(item) #11:

#1: Usei dict, para conseguir ligar um índice à um valor. Vai vendo... rss
#2: Fui obrigado à criar pois "lista = MyList()" não rodaria por conta de "Class MyList(Sequence):".
#3: Mais um que fui obrigado adicionar.
#4: Respostas: getitem: 0 /// Hipácia.
#5: Resposta: 2.
#6: Sem ele, não consigo utilizar o "for".
#7: Sem ele, não consigo usar o "__iter__()".
#8: Incluído p/ trabalhar com "__next__".
#9: Aqui onde usaremos o "_next_index".
#10: Pronto, eliminamos o erro apresentado no bash.
#11: Respostas: Hipácia /// Dienekes.
#12: Para conseguir alterar este valor do índice 0, precisamos adicionar __setitem__.
#13: Adicionamos o __setitem__, agora o código tem que rodar.
#14: Funcionou, conseguimos alterar o valor.
#15: Resposta: Edson.