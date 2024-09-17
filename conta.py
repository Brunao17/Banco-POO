import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.saldo = saldo
        self.conta = conta

    def sacar(self, valor): ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'Deposito {valor}')

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'Saque {valor}')
            return self.saldo  
        print('Nao foi possivel sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
       
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_max = -self.limite

        if valor_pos_saque >= limite_max:
            self.saldo -= valor
            self.detalhes(f'Saque {valor}')
            return self.saldo  
        
        print('Nao foi possivel sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')



if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 0)
    cp1.depositar(1.00)
    cp1.sacar(2.00)
    print('*****')
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.depositar(1.00)
    cc1.sacar(2.00)
    cc1.sacar(99)
    cc1.sacar(1)