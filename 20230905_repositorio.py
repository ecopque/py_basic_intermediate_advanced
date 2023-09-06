from typing import Dict

class Repositorio:
    def select(self, nome: str) -> Dict:
        return {"nome": nome, "idade": 39}
    
    def insert(self, nome: str, idade: int) -> Dict:
        print('Inserindo dados {}, {}'.format(nome, idade))
        return {"nome": nome, "idade": idade}
