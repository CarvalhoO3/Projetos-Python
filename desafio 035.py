total = float(input('Qual a distância desta viagem? '))
if total<=200:
    print('sua viagem custará', total * 0.5,'Reais')
else:
    print('Neste caso, ela será o valor de', total * 0.45,'Reais')