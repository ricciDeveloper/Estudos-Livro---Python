#Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
qtd_cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos_fumante = float(input("Há quantos anos você fuma? "))
minutos = anos_fumante * 365 * qtd_cigarros * 10
# cada dia tem 24 horas * 60 minutos
conversao_dias = minutos / (24*60)

print("Redução do tempo de vida %8.2f dias."%conversao_dias)