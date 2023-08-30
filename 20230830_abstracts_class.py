from abc import ABC, abstractmethod #1: #2:
class Log(ABC): #3:
    @abstractmethod #5:
    def _log(self, msg): ... #4:
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
class LogPrintMixin(Log):
    def _log(self, msg): # 8:
        print(f'{msg} ({self.__class__.__name__})')
# l = Log() #6: #7:
l2 = LogPrintMixin()
l2.log_error('Oi') #9: