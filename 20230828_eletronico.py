# File: eletronico.py
from log import LogPrintMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome #1: Nome protegido dentro da classe, não pretendo usar isso fora.
        self._ligado = False
    
    def ligar(self):
        if not self._ligado:
            self._ligado = True
    
    def desligar(self):
        if self._ligado: # ...is True?
            self._ligado = False

class Smartphone(Eletronico, LogPrintMixin): # Pesquisar herança múltipla?
    def ligar(self):
        super().ligar() #2: Estou repassando a chamda do método para cima. Assim não perdeu a funcionalidade que existe acima.
        if self._ligado:
            msg = f'{self._nome} está ligado.'
            self.log_success(msg)

    
    def desligar(self):
        super().desligar()
        if not self._ligado:
            msg = f'{self._nome} está desligado.'
            self.log_erro(msg)