#Faça um algoritmo que leia os valores de A,B,C e imprima na tela se a soma de A + B é menor que C

a = int((input("Insira um valor para A: ")))
b = int((input("Insira um valor para B: ")))
c = int(input("Insira um valor para C: "))

if a + b < c:
    print(f"A soma de {a} + {b} é menor que {c}")

else:
    print(f"A soma de {a} + {b} não é menor que {c}")
