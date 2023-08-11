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
        
    def __pode_saque(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite 
        return valor_a_sacar <= valor_disponivel_a_sacar
    
    # PRIVANDO METODO PARA NÃO SER USADO FORA DA CLASSE
    def saque(self, valor):
        if self.pode_saque(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))
    
    def tranferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
        
    @property   
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

conta = Conta(123,"Nico", 55.0, 1000.0)
conta2 = Conta(123,"Marco", 100.00, 1000.0)

conta.saque(1200.0)
print(conta.saldo)