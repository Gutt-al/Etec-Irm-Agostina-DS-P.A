# Descreva um algoritmo que leia um numero, subtraia do seu valor o numero 3
# leia outro numero e some ao seu valor o numero 2
# some os resultados das operaçoes realizadas com os numeros lidos, subtraia do resultado
# o numero 1 e mostre em video o valor final da operação

n1 = int(input('Digite um numero: '))
sub1 = n1 - 3
n2 = int(input('Digite outro numero: '))
soma1 = n2 + 2
soma2 = n1 + n2
sub2 = soma2 - 1
print(f'O resultado da operação é: {sub2}')
