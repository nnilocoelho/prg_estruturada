peso = float (input ('Insira seu peso: '))
altura = float (input ('Insira sua altura: '))

formIMC = (peso / (altura * altura))

if 0 > formIMC < 18.5:
    print (f'Seu IMC é {formIMC:.1f}, você está abaixo do peso!')
elif 18.5 >= formIMC < 24.9:
    print (f'Seu IMC é {formIMC:.1f}, você está com peso normal!')
elif 25 >= formIMC < 29.9:
    print (f'Seu IMC é {formIMC:.1f}, você está acima do peso!')
elif formIMC >= 30:
    print (f'Seu IMC é {formIMC:.1f}, você está obeso!')