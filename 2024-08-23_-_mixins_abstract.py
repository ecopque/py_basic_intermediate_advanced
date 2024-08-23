class Log:
    def log(self, msg): #1:
        raise NotImplementedError('Implemente o método log.')
class LogFileMixin(Log):
    def log(self, msg):
        print(msg)
if __name__ == '__main__':
    # l = Log()
    # l.log('Qualquer coisa...') #2:
    k = LogFileMixin() #3:
    k.log('XYZ') #4:
