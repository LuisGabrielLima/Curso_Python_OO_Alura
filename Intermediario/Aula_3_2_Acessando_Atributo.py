class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("contruindo...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta(123,"Nico", 55.0, 1000.0)
conta2 = Conta(123,"Marco", 100.00, 1000.0)

# ACESSAR VALOR DO ATRIBUTO
print(conta.saldo)
print(conta2.saldo)