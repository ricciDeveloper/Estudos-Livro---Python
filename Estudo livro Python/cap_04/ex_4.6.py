#Exercício 4.6 Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas

distancia = float(input("Qual a distância que deseja percorrer?"))
preco_km = ()


if distancia <=200:
    preco_km = 0.50*distancia
    print("O valor a ser pago é de R$%6.2f"%(preco_km))
else:
    preco_km = 0.45*distancia
    print("O valor a ser pago é de R$%6.2f"%(preco_km))