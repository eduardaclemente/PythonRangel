n = int(input("Digite um número inteiro"))
digitos = 0
while n != 0:
    digitos += 1
    n = n // 10
print(digitos)