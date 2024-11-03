#  Crie um algoritmo que leia dois números, multiplique o menor por 10, e divida
# o maior por 2, some os seus valores e verifique se o resultado e par, em caso
# afirmativo exiba a mensagem, o resultado é par, caso contrario, exiba a
# mensagem, o resultado é impar.

'''
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
mult = 0
div = 0
if n1 < n2:
    mult = n1 * 10
else:
    mult = n2 * 10
if n1 > n2:
    div = n1 / 2
else:
    div = n2 / 2
soma = mult + div
res = soma % 2
if res == 0:
    print('O resultado e par!')
else:
    print('O resultado e impar!')
'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
if n1 < n2:
    n1 = n1 * 10
    n2 = n2 / 2
else:
    n1 = n1 / 2
    n2 = n2 * 10
soma = n1 + n2
res = soma % 2
if res == 0:
    print('PAR')
else:
    print('IMPAR')
