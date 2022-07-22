class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao



class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def retorna_cadastro_diferenciado(self):
        pass    


vingadores = Filme("bolinha", 2001, 160)
vingadores.dar_like()
print(f"Filme: {vingadores._nome}, Ano: {vingadores.ano}, Duração: {vingadores.duracao}, likes: {vingadores._likes}")


grey_anatomy = Serie("grey's anatomy", 2005, 19)
grey_anatomy.dar_like()
grey_anatomy.dar_like()
grey_anatomy.nome = "Anatomia da Grey"
print(f"Série: {grey_anatomy.nome}, Ano: {grey_anatomy.ano}, Temporadas: {grey_anatomy.temporadas}, likes:{grey_anatomy._likes}")







