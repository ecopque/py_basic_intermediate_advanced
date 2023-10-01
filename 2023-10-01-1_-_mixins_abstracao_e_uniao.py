class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log.') #1:
class LogFileMixin(Log):
    def log(self, msg):
        print(msg)
if __name__ == '__main__':
    l = LogFileMixin()
    l.log('Qualquer coisa...')