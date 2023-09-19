class MyContextManager():

    def __init__(self):
        print('Init')

    def __enter__(self):
        print('Enter')
        return 123

    def __exit__(self, class_exception, exception_, traceback_):
        print('Exit')

instancia = MyContextManager()

with instancia as alguma_coisa:
    print('With', alguma_coisa) #1:

#1: Resposta: Init | Enter | With 123 | Exit.