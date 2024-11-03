# Elabore um algoritmo que leia dois números e mostre os seus valores
# multiplicados por 10 se a soma dos valores originais for menor que 20.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
r = n1 + n2
if r < 20:
    r2 = r * 10
    print(f'{r2}')
