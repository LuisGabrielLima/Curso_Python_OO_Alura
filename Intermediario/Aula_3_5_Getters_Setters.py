class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("contruindo...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print("Saldo do {} do titular {}".format(self.__saldo, self.__titular))
    
    def deposito(self, valor):
        self.__saldo += valor
        
    def saque(self, valor):
        self.__saldo -= valor
    
    def tranferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
        
    # METODOS GET - DEVOLVE ALGO
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def get_limite(self):
        return self.__limite
    
    # METODOS SET - MODIFICA ALGO
    def set_limite(self, limite):
        self.__limite = limite

conta = Conta(123,"Nico", 55.0, 1000.0)
conta2 = Conta(123,"Marco", 100.00, 1000.0)

print(conta.get_saldo())
print(conta.get_titular())
print(conta.get_limite())

conta.set_limite(10000.0)

print(conta.get_limite())