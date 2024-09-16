vel = float(input('Qual a velocidade que estava seu carro? '))
km = 7
if vel<=80:
    print('Você respeitou os limites, boa viagem!')
else:
    print('Opa, você ultrapassou os limites e pagará ',(vel - 80) * km ,'Reais a ser pago de multa')


