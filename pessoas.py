class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @property
    def nome(self):
        return self._nome
    
    @nome.setter  
    def nome(self, nome:str):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter  
    def idade(self, nome: int):
        self._idade = nome

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'
    

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta: conta.conta | None = None


if __name__ == '__main__':
    import conta
    c1 = Cliente('Luiz', 30)
    print(c1)
    c1.conta = conta.ContaCorrente(111, 222, 0, 0)
    print(c1.conta)