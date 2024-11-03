#  Desenvolva um algoritmo que leia quatro números, some os dois primeiros e
# subtraia os dois últimos, some os resultados e mostre a seguinte mensagem,
# resultado maior que dez, caso a afirmação esteja correta ou resultado menor
# ou igual a dez.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))
n4 = int(input('Digite outro numero: '))
res1 = n1 + n2
res2 = n3 - n4
res3 = res1 + res2
if res3 > 10:
    print('Resultado maior que dez!')
else:
    print('Resultado menor ou igual a dez!')
