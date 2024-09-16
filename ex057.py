sexo = str(input("Qual seu sexo? [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Sexo Inválido,Tente novamente!")).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))