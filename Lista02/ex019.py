'''Construir um algoritmo para calcular as raızes de uma equação do 2o grau,
sendo que os valores dos coeficientes A, B, e C devem ser fornecidos pelo
usuario atraves do teclado.'''

A = int(input('Insira um número para A: '))
B = int(input('Insira um número para B: '))
C = int(input('Insira um número para C: '))

calculoRaiz = (B * B) - 4 * A * C

print('=' * 20)

print(f'B² - 4 x A x C')
print(f'{B ** 2} - {4 * A * C}')
print(f'O resultado é: {calculoRaiz}')


