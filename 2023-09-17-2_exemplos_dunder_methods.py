class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name} (x={self.x!r}, y={self.y!r})'
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other
    
if __name__ == '__main__':
    p1 = Ponto(4, 2) #1:
    p2 = Ponto(6, 4) #2:
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que P2? Resposta:', p1 > p2) #3:

#1: A soma de 4 e 2 = 6.
#2: A soma de 6 e 4 = 10.
#3: Resposta: False.

# Edson Copque | https://linktr.ee/edsoncopque
