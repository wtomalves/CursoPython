import random

import forca


def jogar():
    print("*********************************")
    print("Bem vindo ao Jogo de Adivinhação")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    print(numero_secreto)
    tentativas = 1
    rodada = 3
    total_rodadas = 0
    pontos = 1000
    pontos_perdidos = 0

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_rodadas = 20
    elif (nivel == 2):
        total_rodadas = 10
    else:
        total_rodadas = 3


    for tent in range(1, total_rodadas + 1):

        print("Tentativa {} de {}".format(tent, total_rodadas))
        chute = int(input("Chute um número entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100 ")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print("Você digitou ", chute)



        if (acertou):
            print(f"Parabéns, você acertou e fez {pontos} pontos!")
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute) / 3 # Para números absolutos sem sinal
            pontos = pontos - pontos_perdidos

            if (maior):
                print("Errou! O número digitado foi maior do que o número secreto.")

            elif (chute < numero_secreto):
                print("Errou! O número digitado foi menor do que o número secreto.")




    print(f"Você terminou o jogo com {round(pontos)} pontos!")
    print("Fim do Jogo.")


if (__name__ == "__main__"):
    jogar()

"""
 uSANDO LAÇO DE REPERIÇÃO WHILE
 
 
 numero_secreto = 10
tentativas = 1
rodada = 3
total_rodadas = 3



while (tentativas <= total_rodadas):

    print("Tentativa {} de {}".format(tentativas, total_rodadas))
    chute = int(input("Digite o seu numero: "))
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print("Você digitou ", chute)

    if (acertou):
        print("Parabéns, você acertou o número secreto!")
        break
    else:
        if (maior):
            print("Errou! O número digitado foi maior do que o número secreto.")
        elif (chute < numero_secreto):
            print("Errou! O número digitado foi menor do que o número secreto.")

    tentativas += 1

print("Fim do Jogo.")
"""




"""
for rodadas in range(1, 10, 5):
    print(rodadas)
print("*********")
for c in ["a", "v"]:
    print(c)
"""



