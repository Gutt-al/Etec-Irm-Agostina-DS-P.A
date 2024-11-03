# Elabore um algoritmo que leia um número, se ele for maior que dez, some
# cinco ao seu valor, se for menor ou igual, some 20 e mostre se o resultado for
# maior que vinte e cinco

n = int(input('Digite um numero: '))
res = 0
res1 = 0
if n > 10:
    res = n + 5
if n <= 10:
    res1 = n + 20
if res > 25:
    print(f'{res}')
if res1 > 25:
    print(f'{res1}')
