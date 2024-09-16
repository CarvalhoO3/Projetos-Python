import random
a = str(input('Primeiro Aluno :'))
b = str(input('Segundo Aluno :'))
c = str(input('Terceiro ALuno :'))
d = str(input('Quarto Aluno :'))
lista = [a,b,c,d]
random.shuffle(lista)
print('A ordem escolhida foi')
print(lista)

