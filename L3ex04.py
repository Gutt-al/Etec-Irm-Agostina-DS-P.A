# Crie um algoritmo que leia três números some 5 aos seus valores e mostre os
# valores resultantes maiores que 10.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))
r1 = n1 + 5
r2 = n2 + 5
r3 = n3 + 5
if n1 > 10:
    print(f'{r1}')
if n2 > 10:
    print(f'{r2}')
if n3 > 10:
    print(f'{r3}')
