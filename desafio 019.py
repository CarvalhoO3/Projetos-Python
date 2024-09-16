import random
a = str(input('Primeiro Aluno :'))
b = str(input('Segundo Aluno :'))
c = str(input('Terceiro ALuno :'))
d = str(input('Quarto Aluno :'))
x = [a,b,c,d]
escolhido = random.choice(x)
print('O aluno escolhido foi {}'.format(escolhido))
