# Desenvolva um algoritmo que leia três números e mostre na tela os números
# entre os dois maiores.
'''
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))
if n1 > n2: # n1 maior e os outro são os segundos maiores!
    if n1 > n3:
        if n2 > n3:
            while n2 < n1:
                n2 = n2 + 1
                print(n2)
    if n1 > n3:
        if n1 > n2:
            if n3 > n2:
                while n3 < n1:
                    n3 = n3 + 1
                    print(n3)
    if n2 > n1: # n2 maior e os outro são os segundos maiores!
        if n2 > n3:
            if n1 > n3:
                while n1 < n2:
                    n1 = n1 + 1
                    print(n1)
    if n2 > n1:
        if n2 > n3:
            if n3 > n1:
                while n3 < n2:
                    n3 = n3 + 1
                    print(n3)
    if n3 > n1: # n3 maior e os outro são os segundos maiores!
        if n3 > n2:
            if n1 > n2:
                while n1 < n3:
                    n1 = n1 + 1
                    print(n1)
    if n3 > n1:
        if n3 > n2:
            if n2 > n1:
                while n2 < n3:
                    n2 = n2 + 1
                    print(n2)
else:
    print("Não existe número entre eles!")
'''

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))
if n1 > n2:
    if n1 > n2:
        if n2 > n3:
            while n2 < n1:
                n2 = n2 + 1
                print(n2)
        else:
            while n3 < n1:
                n3 = n3 + 1
                print(n3)
    else:
        if n2 > n1:
            if n1 > n3:
                while n1 < n2:
                    n1 = n1 + 1
                    print(n1)
            else:
                while n3 < n2:
                    n3 = n3 + 1
                    print(n3)
        else:
            if n3 > n1:
                if n1 > n2:
                    while n1 < n3:
                        n1 = n1 + 1
                        print(n1)
                else:
                    while n2 < n3:
                        n2 = n2 + 1
                        print(n2)
else:
    print('Os numeros são iguais ou não tem numeros entre eles!')
'''
alternativas - 8,5,2 - 5,8,2 - 2,8,5 - 2,5,8 - 8,2,5

'''