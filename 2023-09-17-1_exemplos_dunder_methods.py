class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name} (x={self.x!r}, y={self.y!r})'
    
    def __add__(self, other): #1:
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

if __name__ == '__main__':
    p1 = Ponto(4, 2)
    p2 = Ponto(6, 4)
    p3 = p1 + p2 #2:
    print(p3) #3:

#1: "self" será "p1", "other" será "p2". Python faz isso automaticamente.
#2: Entenda: "p1" _add__ "p2". É assim!
#3: Resposta: Ponto (x=10, y=6).

# Edson Copque | https://linktr.ee/edsoncopque
