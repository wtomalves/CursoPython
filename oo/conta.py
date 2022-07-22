class Conta:

    def __init__(self, numero, titular, saldo, limite):  # Método Construtor
        #print("Conntruindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} ultrapassa seu limite.")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property #propriedade
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

    @staticmethod #método da classe
    def codigo_banco():
        return "001"

    @staticmethod  # método da classe
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237', 'Itaú':'341'}



print("*********Conta Nico ***********\n")
conta = Conta(123, "Nico", 55.5, 1000.00)

print("*********Conta Marco ***********\n")
conta2 = Conta(321, "Marco", 100.0, 1000.00)



print(conta2.codigo_banco())
print(conta2.codigos_bancos())








