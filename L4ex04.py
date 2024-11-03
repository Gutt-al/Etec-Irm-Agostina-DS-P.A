# Elabore um algoritmo que leia três números e mostre o maior


n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))
maior = n1
if n2 > n1:
    if n2 > n3:
        maior = n2
if n3 > n1:
    if n3 > n2:
        maior = n3
print(f'O maior numero é {maior}')
