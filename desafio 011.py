n = float(input('Qual o preço do produto?'))
n1 = n - (n * 5 / 100)
print('o produto que custava {:.2f} na promoção com desconto de 5%, vai custar R${}'.format(n,n1))