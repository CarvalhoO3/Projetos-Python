num1 = float(input("Digite sua primeira nota: "))
num2 = float(input("Digite sua segunda nota:"))
média = (num1 + num2) / 2
if média < 5:
    print(" suas notas foram {} e {}, e sua média é {}. Você está reprovado...".format(num1,num2,média))
elif média > 5 <=6.9:
    print(" Suas notas foram {} e {}, e sua média é {}. Você está de recuperação...".format(num1,num2,média))
elif média > 7:
    print ("Suas notas foram {} e {], e sua média é {}. Você está aprovado!!".format(num1,num2,média))
