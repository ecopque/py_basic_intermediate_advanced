import enum

Direcoes = enum.Enum('Direcional', ['ESQUERDA', 'DIREITA']) #2: #3: #4:
def mover(direcao):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Não encontrei essa direção, amiguinho(a)!') #1:
    print(f'Movendo para {direcao}')

mover(Direcoes.ESQUERDA) #5:
mover(Direcoes.DIREITA) #6:
print(Direcoes(1)) #7: #9:
print(Direcoes(2)) #8: #10:
print(Direcoes['ESQUERDA']) #11: #12:
print(Direcoes.ESQUERDA) #13: #14:
print(Direcoes(1).name) #15:
print(Direcoes.DIREITA.value) #16:

#1: Jogue o erro na tela, para o bug não passar despercebido! Se liga, tio.
#2: Perceba: enum.Enum é módulo e classe.
#3: 'Direcoes' é nome do tipo e [''] são os valores.
#4: Como estou criando enum e este é constante (membros), vou atribuir como: 'ESQUERDA', 'DIREITA', ou seja, não é p/ mudar.
#5: Resposta: Movendo para Direcional.ESQUERDA.
#6: Resposta: Movendo para Direcional.DIREITA.
#7: Resposta: Direcional.ESQUERDA
#8: Resposta: Direcional.DIREITA.
#9: Ref: NomeDaEnum(valor_enum) -> MEMBRO.
#10: Ref: NomeDaEnum(valor_enum) -> MEMBRO.
#11: Resposta: Direcional.ESQUERDA.
#12: Ref: NomeDaEnum['chave'] - MEMBRO.
#13: Resposta: Direcional.ESQUERDA.
#14: Ref: Iiih, funcionou! ;-)
#15: Resposta: ESQUERDA.
#16: Resposta: 2.




"""
#Explicação (linkedin): Enumerações (enum) na programação são utilizadas quando precisamos representar um conjunto fixo e predefinido de opções. Elas não são criadas p/ serem usadas como "dict" (dicionários). Pense assim: enums possuem membros que possuem valores constantes e simbólicos. Dá p/ pensar neles como um grupo de nomes vinculados a valores exclusivos e fixos.

Essencialmente, dá p/ entender que "enum" é uma coleção de identificadores simbólicos, cada um associado a um valor único e constante. Você pode "iterar" através de uma enumeração p/ acessar seus membros na ordem em que foram definidos. 

enum.Enum é a superclasse p/ suas enumerações, mas dá p/ usá-las diretamente. No entanto, perceba: enums não são classes normais em Python. 

Até agora, consegui perceber que dá p/ usar enums com "type annotations", verificar tipos com "isinstance" e realizar outras operações relacionadas ao tipo (type).

Mas e aí, como acessar os dados de uma enumeração? Assim:

* Para obter um membro específico: membro = NomeDaEnum(valor_enum) ou NomeDaEnum['chave'] -> (semelhante a dict);

* Para obter a chave de um membro: chave = NomeDaEnum.membro.name;

* Para obter o valor de um membro: valor = NomeDaEnum.membro.value.

Obs: entenda NomeDaEnum como a Classe.

"""