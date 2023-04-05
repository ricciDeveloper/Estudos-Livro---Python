#Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado
km_percorridos = float(input("Quantos Km foram percorridos com o carro? "))
qtd_dias = int(input("Quantos dias permaneceu com o carro em locação? "))
preco_km = km_percorridos * 0.15
preco_dias = qtd_dias*60
valor_total = int(preco_km+preco_dias)
print("Você percorreu o toal de %.2fKm, e ficou com o carro por %d dias, totalizando o valor de alguel em R$%.2f"%(km_percorridos, qtd_dias, valor_total))