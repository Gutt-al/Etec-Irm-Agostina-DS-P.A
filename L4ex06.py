#Desenvolva um algoritmo que leia dois números e mostre os números em
# ordem crescente.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 < n2:
    print(f'{n1}, {n2}')
else:
    print(f'{n2}, {n1}')
