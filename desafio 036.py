casa = float(input('valor da casa: R$'))
salario = float(input('E o salário é quanto? '))
anos = int(input('Quantos anos deseja pagar a casa?'))
resultado = casa / (anos * 12)
minimo = salario * 30/100
print('Olha, o valor da casa é {:.2f}R$ em {} anos, a prestação será de R${:.2f}'. format(casa, anos, resultado))
if resultado <= minimo:
        print('Empréstimo Concedido!!')
else:
        print('Empréstimo Negado!')