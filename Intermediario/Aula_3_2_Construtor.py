class Conta:
    
    # FUNÇÃO CONSTRUTORA
    def __init__(self, numero, titular, saldo, limite): # SELF É O VALOR DA REFERENCIA DO MEU OBJETO EM MEMORIA
        print("contruindo...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta(123,"Nico", 55.0, 1000.0)
conta2 = Conta(123,"Marco", 100.00, 1000.0)