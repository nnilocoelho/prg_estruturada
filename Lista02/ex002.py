"""Faca um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa.
Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de
casada (anos)."""

nome = input('Insira seu nome: ')
sexo = input('Insira seu sexo: ')
estadoCivil = input('Insira seu estado civil: ')

if sexo == "F" and estadoCivil == "CASADA":
    tempoCasada = int(input('Insira seu tempo de casamento: '))
    print(f'Olá {nome}, seu gênero é {sexo}, você é {estadoCivil} e tem {tempoCasada} anos de casamento. ')
else:
    print(f'Olá {nome}, seu gênero é {sexo}, e seu estado civil é {estadoCivil}')



