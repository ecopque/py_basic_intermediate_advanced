from datetime import date
class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento #2:
      
    def dias_vividos(self):
        return (date.today() - self.data_nascimento).days #1:

    @property #5:
    def data_nascimento(self): #6:
        return self._data_nascimento #7:
    
    @data_nascimento.setter # 8:
    def data_nascimento(self, value): #10: #11:
        if not isinstance(value, date): #14:
            raise ValueError('data_nascimento deve ser um objeto do tipo date.')
        self._data_nascimento = value #12: #13:
        
# p1 = Pessoa('Mel', date(2000, 8, 30)) #3: #4:
p2 = Pessoa('Théo', '2000/08/30') #9: #15:
print(p2.dias_vividos())