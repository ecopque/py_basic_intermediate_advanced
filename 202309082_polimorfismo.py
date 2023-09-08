class Pato(object):
    def grasnar(self):
        print('Quack, quack')
    def voar(self):
        print('Flap, flap')
class Pessoa(object):
    def grasnar(self):
        print('Estou imitando um pato: guaqui, guaqui.')
    def voar(self):
        print('Estou imitando um pato: batendo os braços.')
def grasnar_e_voar(parametro):
    if isinstance(parametro, Pato):
        parametro.grasnar()
        parametro.voar()
    else:
        print('O objeto tem que ser um pato')
pato = Pato()
grasnar_e_voar(pato) #1:
pessoa = Pessoa()
grasnar_e_voar(pessoa) #2:

#1: Resposta: Quack, quack | Flap, flap.
#2: Resposta: O objeto tem que ser um pato.