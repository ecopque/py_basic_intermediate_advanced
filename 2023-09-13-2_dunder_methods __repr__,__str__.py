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
print(p2) #2:

#1: Resposta: (3, 6).
#2: Resposta: (123, 789).

# Edson Copque | https://linktr.ee/edsoncopque
