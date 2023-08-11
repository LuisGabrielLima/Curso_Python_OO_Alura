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
        # SELF É USADO TANTO PARA ATRIBUTOS QUANTO PARA METODOS
        self.saque(valor)
        destino.deposito(valor)

conta = Conta(123,"Nico", 55.0, 1000.0)
conta2 = Conta(123,"Marco", 100.00, 1000.0)

conta.extrato()
conta2.extrato()

conta2.tranferencia(10.00, conta)

conta.extrato()
conta2.extrato()