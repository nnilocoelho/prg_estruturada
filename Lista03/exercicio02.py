contador = n = soma = 0

while n <= 10:
    n = int(input('Digite um número: '))
    soma += n
    contador += 1
    if contador == 10:
        break


print('No total, foram {} números digitados e a soma entre eles é {}.'.format(contador, soma))

