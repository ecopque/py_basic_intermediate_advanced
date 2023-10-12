from dataclasses import dataclass, field, fields

@dataclass
class Pessoa:
    nome: str = 'Carl'
    sobrenome: str = 'Sagan'
    idade: int = 0
    # endereco1: list[str] = [] #1: #2:
    endereco2: list[str] = field(default_factory=list) #3:
    tamanho: str = field(default='1,80', repr=False) #4:

if __name__ == '__main__':
    p1 = Pessoa()
    print(p1) #6:
    print(fields(p1)) #5:

#1: Não iria funcionar, afinal de contas @dataclass obrigatoriamente é imutável (contrário de lista).
#2: Resposta referente à essa linha de código: raise ValueError(f'mutable default {type(f.default)} for field '. ValueError: mutable default <class 'list'> for field endereco1 is not allowed: use default_factory.
#3: A fábrica da coisa mutável.
#4: Usando "field" e apontando "__repr__" como false, não será apresentado na saída.
#5: Com field, será apresentado os metadados.
#6: Resposta: Pessoa(nome='Carl', sobrenome='Sagan', idade=0, endereco2=[]).
#7: Resposta: (Field(name='nome',type=<class 'str'>,default='Carl',default_factory=<dataclasses._MISSING_TYPE object at 0x7fb1b64d27c0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), Field(name='sobrenome',type=<class 'str'>,default='Sagan',default_factory=<dataclasses._MISSING_TYPE object at 0x7fb1b64d27c0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), Field(name='idade',type=<class 'int'>,default=0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fb1b64d27c0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), Field(name='endereco2',type=list[str],default=<dataclasses._MISSING_TYPE object at 0x7fb1b64d27c0>,default_factory=<class 'list'>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), Field(name='tamanho',type=<class 'str'>,default='1,80',default_factory=<dataclasses._MISSING_TYPE object at 0x7fb1b64d27c0>,init=True,repr=False,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)).


