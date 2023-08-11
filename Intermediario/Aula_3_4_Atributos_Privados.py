class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("contruindo...{}".format(self))
        # PRIVAR ATRIBUTO   >   PARA ACESSAR DIRETAMENTE DEVE USAR _"Nome da Classe"__"Atributo"
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

conta = Conta(123,"Nico", 55.0, 1000.0)
conta2 = Conta(123,"Marco", 100.00, 1000.0)