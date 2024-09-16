km = float(input('Quantos km você percorreu com este carro?'))
dia = int(input('E quantos dias você o utilizou?'))
total = (dia*60 + km*0.15)
print('Você o utilizou por {} dias e andou por {} km, com isso irá pagar um total de R${:.2f}'.format(dia, km, total))