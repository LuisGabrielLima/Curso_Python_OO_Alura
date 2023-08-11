class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("contruindo...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extrato(self):
        print("Saldo do {} do titular {}".format(self.saldo, self.titular))
    
    def deposito(self, valor):
        self.saldo += valor
        
    def saque(self, valor):
        self.saldo -= valor

conta = Conta(123,"Nico", 55.0, 1000.0)
conta2 = Conta(123,"Marco", 100.00, 1000.0)

# USAR METODOS DA CLASSE
conta.extrato()
conta2.extrato()

conta.deposito(15.00)
conta.extrato()

conta.saque(15.00)
conta.extrato()

