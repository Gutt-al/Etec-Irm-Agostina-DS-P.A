# Crie um algoritmo que leia três números, some seus valores e mostre o
# resultado se ele for maior que 20.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))
r = n1 + n2 + n3
if r > 20:
    print(f'{r}')
