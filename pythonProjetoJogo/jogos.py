
import forca
import adivinhacao

def escolha_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Selecione o jogo: "))

    if (jogo ==  1):
        print("Jogando o jogo da Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando o jogo da Adivinhação")
        adivinhacao.jogar()

    print("Carregandooooo!")

if (__name__ == "__main__"):
    escolha_jogo()
