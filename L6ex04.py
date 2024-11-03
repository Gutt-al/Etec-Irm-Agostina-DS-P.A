# Elabore um algoritmo que leia um número e mostre a tabuado do número lido,
# utilizando uma estrutura de repetição.

# Jeito de uma aluna:

'''
x = int(input("Digite um número: "))
y = x * 11
a = x
while a < y:
    print(a)
    a = a + x
'''

# feito por mim

n = int(input("Digite um número: "))
cont = 0
while cont < 10:
    cont = cont + 1
    r = n * cont
    print(f"{n} x {cont} = {r}")
