import random

def jogar():
    print("*********************************")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Facíl (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou o número", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve chutar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou!")
            print("Você fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()