class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome
    
    # PROPRIEDADE DO GET
    @property  
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()
    
    # PROPRIEDADE DO SET
    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome
        
# SET
cliente = Cliente("nico")
print(cliente.nome)

# GET
cliente = Cliente("nico")
cliente.nome = "marco"
print(cliente.nome)


# APLICANDO NO CODIGO

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
        
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

conta = Conta(123,"Nico", 55.0, 1000.0)
conta2 = Conta(123,"Marco", 100.00, 1000.0)

print(conta.limite)
conta.limite = 2000.0
print(conta.limite)