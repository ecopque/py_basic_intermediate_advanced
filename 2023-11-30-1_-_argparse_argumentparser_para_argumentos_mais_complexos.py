import argparse #ArgumentParser

var_parser = argparse.ArgumentParser() #1:
var_parser.add_argument('-b', '--basic', #2: #13:
                        help = 'Msg de help!',
                        type = str,
                        metavar = 'String', #14: #15:
                        default = 'Msg de default!', #16:
                        required=True, #17:
                        nargs='+') #18:
var_args = var_parser.parse_args() #3:

print(var_args) #4: #5: | #7: #8:
print(var_args.basic) #6: | #9:

if var_args.basic is None: #10: #11: #12:
    print('Você não passou o valor de "b"')
else:
    print(f'O valor de "var_args.basic" é:', var_args.basic)



#1: "argparse.ArgumentParser()" é uma classe que facilita a análise de argumentos da linha de comando. Aqui vai criar um objeto que contém informações sobre os argumentos e opções que o programa pode aceitar.
#2: "x.add_argument('')" é uma função usada para especificar quais argumentos o programa pode aceitar. No exemplo, o argumento adicionado é um argumento opcional '-b' ou '--basic' na linha de comando.
#3: "x.parse_args()" é um método usado para analisar os argumentos da linha de comando especificados por meio da configuração do "argparse.ArgumentParser()".
#4: Neste primeiro momento, vou rodar no terminal: $ python3 main.py (sem argumentos). Abaixo, as respostas.
#5: Resposta: Namespace(b=None).
#6: Resposta: None.

#7: Agora vamos rodar o comando no bash: $ python3 main.py -b 789 (também podemos usar --basic, até prefiro), onde "-b" é chave e "789" valor. #8: e #9: com as respostas.
#8: Resposta: Namespace(b='789').
#9: Resposta: 789.

#10: Terminal: Se não passar valor de "b", teremos negativa. Se passar, teremos o valor de "var_args".
#11: Agora rodei/terminal: $ python3 main.py --basic 456.
#12: Resposta: O valor de "var_args.basic" é: 456.
#13: Agora podemos usar no terminal "b" ou "--basic". "--basic" lembra "--help", vamos por aí.

#14: Agora incluí "help", "type" e "metavar".
#15: Após rodar no terminal ($ python3 main.py --help), recebemos algumas orientações: -b String, --basic String | Msg de help!.

#16: Se agora rodar $ python3 main.py (sem argumentos) receberei a mensage de "default": Msg de default!
#17: Se "required=True", serei obrigado à inserir os argumentos no terminal.
#18: Com "nargs='+'" vamos permitir mais de um argumento, ex: [python3 main.py --basic 1 + 2 + 3].

#Documentação: https://docs.python.org/pt-br/3/howto/argparse.html