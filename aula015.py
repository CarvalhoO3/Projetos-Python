"""n = s = 0
while True: # 999 é o flag ou seja é o ponto de parada do programa, caso ficar while True, fará sem o programa de parada
    n = int(input("Digite um número: "))
    if n == 999:
        break # exemplo de como usar break, como parar o programa onde é desejado
    s+= n
  #print("A soma vale {}".format(s))
print(f"A soma vale {s}") # exemplo de como usar uma forma diferente de print, invés do .format"""
nome = "José"
idade = 33
print("O {} tem {} anos.".format(nome, idade)) # primeiro jeito possível
print(f"O {nome} tem {idade} anos.") #outro exemplo
