'''Tendo como dados de entrada a altura e o sexo de uma pessoa, construa
um algoritmo que calcule seu peso ideal, utilizando as seguintes formulas:
• para homens: (72.7 ∗ h)–58.
• para mulheres: (62.1 ∗ h)–44.7.'''

altura = float(input("DIGITE A SUA ALTURA:  "))
sexo = (input("DIGITE O SEU SEXO: "))

if sexo.lower() == 'Masculino'.lower(): #lower aceita os dados tanto em MAIUSCULO ou minusculo
    pesoIdeal = ((72.7*altura)-58)
    print(f"PESO IDEAL = {pesoIdeal:.2f}Kg")

elif sexo.lower() == "Feminino".lower():
    pesoIdeal = ((62.1 * altura)-44.7)
    print(f"PESO IDEAL = {pesoIdeal:.2f}Kg")
else:
    print("INFORMAÇÕES INVALIDAS")




