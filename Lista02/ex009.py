'''Construa um algoritmo que dado quatro valores A, B , C e D imprima em tela o maior e menor valor'''

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
d = int(input("Digite o valor de D: "))

if a > b:
    a = b

if  c > a:
    a = c

if  d > a:
    a = d

print(f"Maior: {a}")

if b < a:
    a = b
if c < a:
    A = C
if d < a:
    a = d

print(f'Menor: {a}')
