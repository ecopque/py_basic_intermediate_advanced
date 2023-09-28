class A:
    atributo_a = 'Valor A'
    def metodo(self):
        print('A')
class B(A): #1:
    atributo_b = 'Valor B'
    def metodo(self):
        print('B')
class C(B): #2:
    atributo_c = 'Valor C'
    def metodo(self):
        super(C, self).metodo() #3:
        print('C')
c = C()
print(c.atributo_a) #4:
print(c.atributo_b) #5:
print(c.atributo_c) #6:
c.metodo() #7:
