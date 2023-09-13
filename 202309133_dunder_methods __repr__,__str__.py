class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'    
    def __repr__(self):
        class_name = self.__class__.__name__
        class_name2 = type(self).__name__
        return f'{class_name}(x={self.x}, y={self.y})'
p1 = Ponto(3, 6)
p2 = Ponto(123, 789)
print(p1) #1:
print(repr(p2)) #2: #3: #4:
print(f'{p2!s}') #5: #6:
print(f'{p2!r}') #7: #8:

#1: Resposta: (3, 6).
#2: Aqui estamos utilizando "repr()".
#3: Resposta: Ponto(x=123, y=789).
#4: Observe que essa resposta é igual ao método __repr__ da classe "Ponto".
#5: Solicitando print tipo método __str__.
#6: Resposta: (123, 789).
#7: Solicitando print tipo método __repr__.
#8: Resposta: Ponto(x=123, y=789).