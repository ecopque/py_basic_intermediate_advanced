from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar() #1:
    if notificacao_enviada is True:
        print('Notificação enviada.')
    else:
        print('Notificação não enviada.')

n = NotificacaoSMS('Testando notificação!')
n.enviar() #2:

notificacao_email = NotificacaoEmail('Testando e-mail.')
notificar(notificacao_email) #3: 

notificacao_sms = NotificacaoSMS('Testando SMS.')
notificar(notificacao_sms) #4: 

#1: Bool. Ou seja, True ou False.
#2: Resposta: SMS: enviando -  Testando notificação!
#3: Resposta: E-mail: enviando -  Testando e-mail. | Notificação enviada.
#4: Resposta: SMS: enviando -  Testando SMS. | Notificação não enviada.