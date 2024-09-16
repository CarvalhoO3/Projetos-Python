from time import sleep
def contagem_regressiva(n):
    while n >= 0:
        print(n)
        sleep(1)  # Aguarda 1 segundo
        n -= 1
# Iniciar a contagem regressiva de 10
contagem_regressiva(10)
#demonstra o final
print("BOOMM POWW KAPOWW!!")