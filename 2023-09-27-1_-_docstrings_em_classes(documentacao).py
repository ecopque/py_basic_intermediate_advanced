"""Este é um módulo de exemplo (temp.py).

Neste campo vamos trabalhar a descrição do nosso módulo.
"""
variavel_1 = 1
class Foo: #1:
    def soma(self, x: int or float, y: int or float) -> int or float:
        """* Documentação dentro da função "soma()".
        * Neste campo vamos trabalhar a documentação de nossa função "soma()".
        """
        return x + y
    def multiplica(
        self,
        x: int or float,
        y: int or float,
        z: int or float or None = None
    ) -> int or float:
        """* Documentação dentro da função "multiplica()".
        * Neste campo vamos trabalhar a documentação de nossa função "multiplica()".
        """
        if z is None:
            return x * y
        return x * y * z
variavel_2 = 2
variavel_3 = 3
variavel_4 = 4

#1: Pronto, criamos nossa classe e o que antes era função agora se converteu em método. Incluí um self, pois é obrigatório, e temos a seguinte saída conforme imagem.
