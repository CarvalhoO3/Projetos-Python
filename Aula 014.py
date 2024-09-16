'''for c in range(1, 10):
    print(c)
    print('Fim')''' #exemplo1

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print ('Fim')''' #exemplo2
#quando eu não sei, o limite, é melhor usar o while, mas quando eu tenho noção do limite e até quando posso ir, é interessante utilizar o for.

'''for c in range(1,5):
    n = int(input('Digite um valor: ')
print('Fim')''' #exemplo3

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')''' #enquanto não chegar o valor, ele vai lendo até chegar #exemplo4

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
             paxr += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar)) #exemplo5