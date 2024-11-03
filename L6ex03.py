# Crie um algoritmo que leia dois números e mostre os números entre eles.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
if n1 < n2:
    while n1 < n2:
        n1 = n1 + 1
        print(n1)
else:
    while n2 < n1:
        n2 = n2 + 1
        print(n2)
