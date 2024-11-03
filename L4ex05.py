# Elabore um algoritmo que leia três números some cinco ao menor valor e
# mostre o resultado.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))
menor = n1
if n2 < n1:
    if n2 < n3:
        menor = n2
if n3 < n1:
    if n3 < n2:
        menor = n3
menor = menor + 5
print(f'O menor numero somado a 5 é {menor}')
