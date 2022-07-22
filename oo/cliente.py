class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome



cliente = Cliente("marco")
print(cliente.nome)

cliente.nome = "Tom"
print(cliente.nome)


