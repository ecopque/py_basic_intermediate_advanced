class Pai1:
    def metodo_pai1(self):
        print("Método do Pai 1")
class Pai2:
    def metodo_pai2(self):
        print("Método do Pai 2")
class Filha(Pai1, Pai2):
    def metodo_filha(self):
        print("Método da Filha")
obj = Filha() #1:
obj.metodo_filha() #2:
obj.metodo_pai1() #3:
obj.metodo_pai2()

# Edson Copque | https://linktr.ee/edsoncopque
