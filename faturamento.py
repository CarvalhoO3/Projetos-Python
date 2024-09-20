def calcular_faturamento(faturamento):

    faturamento_valido = [dia for dia in faturamento if dia > 0]

    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    media_mensal = sum(faturamento_valido) / len(faturamento_valido)

    dias_acima_da_media = len([dia for dia in faturamento if dia > media_mensal])

    return menor_faturamento, maior_faturamento, dias_acima_da_media

faturamento_diario = [
    1000, 2000, 0, 3000, 1500, 0, 2500, 4000, 1200, 0,
    5000, 6000, 700, 0, 3000, 0, 0, 4500, 600, 800,
    2000, 0, 100, 1500, 0, 0, 3500, 2200, 1800, 0
]

menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
