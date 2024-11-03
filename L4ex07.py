# Crie um algoritmo que leia três números e mostre seus valores em ordem
# crescente.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))
if n1 < n2:
    if n1 < n3:
        if n2 < n3:
            print(f'{n1}, {n2}, {n3}')
        else:
            print(f'{n1}, {n3}, {n2}')
if n2 < n1:
    if n2 < n3:
        if n1 < n3:
            print(f'{n2}, {n1}, {n3}')
        else:
            print(f'{n2}, {n3}, {n1}')
if n3 < n1:
    if n3 < n2:
        if n1 < n2:
            print(f'{n3}, {n1}, {n2}')
        else:
            print(f'{n3}, {n2}, {n1}')
