class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log.')
    def log_erro(self, msg):
        return self._log(f'Erro: {msg}')
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_erro('Usando log_erro!')
    l.log_success('Usando log_success!')

# Edson Copque | https://linktr.ee/edsoncopque
