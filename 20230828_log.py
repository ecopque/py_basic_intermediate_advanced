# File: log.py
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt' #1:

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log.')
    def log_erro(self, msg):
        return self._log(f'Erro: {msg}')
    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo: #4:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_erro('Usando log_erro em LP.')
    lp.log_success('Usando log_success em LP.')

    lf = LogFileMixin()
    lf.log_erro('Usando log_erro em LF.')
    lf.log_success('Usando log_success em LF.')
    print(LOG_FILE) #3: