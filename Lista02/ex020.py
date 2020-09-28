'''Criar um algoritmo que leia numeros inteiros e escreva o dia da semana correspondente, caso o usuário
digite fora deste intervaldo, deve aparecer uma mensagem informando que não existe o dia da semana com este numero'''

numeroDia = int(input("DIGITE O NUMERO CORRESPONDENTE AO DIA DA SEMANA: "))

if numeroDia == 1:
    print('Segunda-feira')

elif numeroDia == 2:
    print('Terça-feira')

elif numeroDia == 3:
    print('Quarta-feira')

elif numeroDia == 4:
    print('Quinta-feira')

elif numeroDia == 5:
    print('Sexta-feira')

elif numeroDia == 6:
    print('Sábado')

elif numeroDia == 7:
    print('Domingo')

else:
    print("Não existe o dia da semana com este numero.")