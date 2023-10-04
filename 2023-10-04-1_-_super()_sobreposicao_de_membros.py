class MinhaString(str):
    def upper(self):
        print('Chamou upper()')
        retorno = super().upper() #1:
        retorno2 = super(MinhaString, self).upper() #(1) #2:
        print('Depois do upper()')
        return retorno
string = MinhaString('Mel')
print(string.upper()) #3: