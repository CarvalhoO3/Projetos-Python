soma_pares = 0
# Lendo 6 números inteiros do usuário
for i in range(6):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    # Verificando se o número é par
    if numero % 2 == 0:
        # Adicionando à soma se for par
        soma_pares += numero
# Mostrando a soma dos números pares
print(f"A soma dos números pares é {soma_pares}")