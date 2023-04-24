n = int(input("Digite o número: "))

def testar_par(a):
    return a%2 == 0

if testar_par(n):
    print (n, "é par")
else:
    print(n, "é ímpar")