num = int(input('Digite um número inteiro: '))
print('''Escolha a operacão desejada\n 1[Binário]\n 2[Octal]\n 3[Decimal]''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print(('{} convertido para decimal é {}'.format(num, hex(num)[2:])))
else:
    print ('Opção Inválida, tente novamente...')