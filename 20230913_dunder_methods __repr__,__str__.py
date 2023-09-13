class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        class_name = self.__class__.__name__ #1:
        class_name2 = type(self).__name__ #2: #3:
        return f'{class_name}(x={self.x}, y={self.y})'
p1 = Ponto(3, 6)
p2 = Ponto(123, 789)
print(p1) #4:
print(p2) #5:

#1: Trazendo o nome da classe.
#2: Idem ao #1, mas prefiro o #1.
#3: Deixei ocioso, não estou usando pois decidi utilizar o #1.
#4: Resposta: Ponto(x=3, y=6).
#5: Resposta: Ponto(x=123, y=789).