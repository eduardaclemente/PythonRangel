import random

numero_certo = random.randint(1,10)
acertou = False
tentativas = 0

while acertou != True:
    tentativas += 1
    palpite = int(input("Digite um número inteiro entre 1 e 10: "))
    if palpite == numero_certo:
        print("Você acertou o número", numero_certo, "em", tentativas, "tentativas!!")
        acertou = True

print()
print("o fim do programa")