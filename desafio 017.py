from math import sqrt
catetox = float(input('Digite o valor do cateto oposto : '))
catetoy = float(input('Digite o valor do cateto adjacente e descubra sua hipotenusa :'))
hipotenusa = (catetox * catetox) + (catetoy * catetoy)
raiz = sqrt(hipotenusa)
print('O valor da sua hipotenusa é {:.2f}'.format(raiz))