''' Ler trẽs valores inteiros e diferentes e mostrar em ordem descrente'''

a = int(input("Insira o primeiro numero inteiro: "))
b = int(input("Insira o segundo numero inteiro: "))
c = int(input("Insira o terceiro numero inteiro: "))

if a < b < c:
    print(f'{c},{b},{a}')

elif a > b > c:
    print(f'{a},{b},{c}')

elif b < a < c:
    print(f'{c},{a}{b}')

