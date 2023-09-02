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

#1: Com "days" Vai me retornar os dias (e não a data).
#2: Com getter vamos printar a data de nascimento. Com setter vamos definir seu valor.
#3: Resposta: 8401.
#4: Esta seria uma forma correta, mas e se colocarmos uma string? Analise abaixo!
#5: Aqui vamos definir o getter. Próximo passo será definir o setter.
#6: Vamos usar o nome da variável que queremos trabalhar.
#7: Aqui poderia colocar qualquer nome, mas por convenção vamos usar o nome da função com underline.
#8: Aqui o nosso decorador, agora temos um setter. Temos que usar o mesmo nome do método.
#9: Como usamos uma string no lugar da data, vamos trabalhar com getter e setter.
#10: Precisa do "value" para atribuirmos um valor que vai para dentro da minha variável.
#11: É por essa função que o valor irá até "self.data_nascimento" da classe pai.
#12: Esse carinha aqui é o mesmo da variável do property. Fique atento!
#13: Aqui colocarmos = value pois será o valor recebido.
#14: Se "value" não for uma instância de "date"… 
#15: Resposta neste trajeto: ValueError: data_nascimento deve ser um objeto do tipo date.
