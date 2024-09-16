from datetime import date
atual = date.today().year
ano = int(input("Qual seu ano de nascimento: "))
idade = atual - ano
print("quem nasceu no ano de {}, tem {} em 2024".format(ano, idade))
if idade < 18:
    saldo = 18 - idade
    print("Não está na hora ainda, espera mais {} anos".format(saldo))
elif idade == 18:
    print("Está no ano certo de se alistar!!")
elif idade > 18:
    saldo = idade - 18
    print("Já passou da hora de se alistar, você se atrasou {} anos".format(saldo))
