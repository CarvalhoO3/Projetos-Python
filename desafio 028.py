import time
from random import randint
computador = randint (0, 5) # pensamento computador
print('-=-' * 20)
print('vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(3)
if jogador == computador:
    print('você acertou!!')
else:
    print('Eu ganhei! eu pensei no número {} e não no {}'.format(computador,jogador))