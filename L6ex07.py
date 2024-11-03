# Elabore um algoritmo que leia dois números, um maior que dez e outro menor
# que 5, mostre os números lidos.

# 1 forma
'''n1 = int(input("Digite um numero: "))
while n1 < 10:
    n1 = int(input("Digite um numero novamente: "))
n2 = int(input("Digite outro numero: "))
while n2 > 5:
    n2 = int(input("Digite outro numero novamente: "))
print(n1,n2)'''

# 2 Forma

n1 = int(input("Digite um numero: "))
if n1 > 10:
    n2 = int(input("Digite outro numero: "))
    if n2 < 5:
        print(n1, n2)
    else:
        if n2 > 10:
            while n2 > 5:
                n2 = int(input("Digite outro numero novamente: "))
        print(n1, n2)
else:
    if n1 > 5:
        while n1 > 5:
            n1 = int(input("Digite um numero novamente: "))
            if n1 > 10:
                n2 = int(input("Digite outro numero: "))
                while n2 > 5:
                    n2 = int(input("Digite outro numero novamente: "))
                print(n1, n2)
    else:
        n2 = int(input("Digite outro numero: "))
        while n2 < 10:
            n2 = int(input("Digite outro numero novamente: "))
        print(n1, n2)
