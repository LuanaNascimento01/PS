import json

with open('faturamento.json', 'r') as file:
    faturamento_dados = json.load(file)
print(faturamento_dados)

faturamento_valores = [dia['faturamento']for dia in faturamento_dados if dia ['faturamento']>0]

menor_faturamento = min(faturamento_valores)
maior_faturamento = max(faturamento_valores)

media_faturamento = sum(faturamento_valores) / len(faturamento_valores)

dias_acima_da_media = sum(faturamento_valores) / len(faturamento_valores)

dias_acima_da_media = sum(1 for valor in faturamento_valores if valor > media_faturamento)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
print(f"Média de faturamento: {media_faturamento}")



