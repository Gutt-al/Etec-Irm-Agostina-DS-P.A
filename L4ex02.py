n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
r1 = n1 + 0
r2 = n2 + 0
if n1 < n2:
    r1 = r1 + 5
else:
    r2 = r2 + 5
if r1 > r2:
    print(f"{r1}")
else:
    print(f"{r2}")
