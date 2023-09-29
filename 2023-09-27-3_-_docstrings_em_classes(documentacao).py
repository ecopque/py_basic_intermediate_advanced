"""* Documentação do módulo (temp.py).

* Neste campo vamos trabalhar a descrição do nosso módulo.
"""
variavel_1 = 1
class Foo: #1:
    """* Documentação da nossa classe.

    * Neste campo vamos trabalhar a descrição da nossa classe.
    """
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
    
    def chopp(self) -> int:
        """ O que este método faz:
        : raises NotImplementedError: Receberemos caso o método não seja definido.
        : raises ValueError: Retorno caso o valor não seja definido, bla!
        """
        raise NotImplementedError('Errou, tio!')


variavel_2 = 2
variavel_3 = 3
variavel_4 = 4
