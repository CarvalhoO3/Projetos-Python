n1 = float(input('Digite a primeira nota :'))
n2 = float(input('Digite a segunda nota :'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Olha sua nota {:.1f} está na média'.format(m))
else:
    print('Olha sua nota {} não está na média'.format(m))
