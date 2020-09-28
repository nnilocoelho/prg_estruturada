'''Um hotel cobra R$ 300,00 por diaria e mais uma taxa adicional de servicos.
Se a diaria for menor que 15 a taxa e de R$ 20,00. Se o numero de diarias for igual a 15 a taxa é de R$ 14,00
e se o numero for maior que 15 a taxa é de R$ 12,00.

Considerando-se que para cada pessoa tenha-se um registro contendo seu nome e o n´umero de di´arias. Faca um algoritmo que
imprima na tela o nome e o total a pagar do hospede.'''

print("Valor Diária R$300")
print("Taxas de Serviços < 15 dias R$20")
print("Taxas de Serviços = 15 dias R$14")
print("Taxas de Serviços > 15 dias R$12")

nome = input("Nome do Hospede: ")
dias = int(input("Informar o numero de diarias: "))

calculoDiaria = dias * 300

if dias < 15:
    print(f'Olá, {nome}, o valor Total + Taxas de Serviços é: R${calculoDiaria+20:.2f}')

elif dias >= 15:
    print(f'Olá, {nome}, o valor Total + Taxas de Serviços é: R${calculoDiaria+14:.2f}')

elif dias > 15:
    print(f'Olá, {nome}, o valor Total + Taxas de Serviços é: R${calculoDiaria+12:.2f}')
