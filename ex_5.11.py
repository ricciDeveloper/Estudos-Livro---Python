#Exercício 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período and\


deposito_inicial = float(input("Qual déposito incial: "))
juros = float(input("Qual juros mensais da poupança: "))


meses = 1
saldo = deposito_inicial

while meses <=24:
    saldo = saldo + (saldo *(juros/100))
    
    print(f"Saldo do mês {meses} é de R${saldo:5.2f}.")
    meses = meses+1


print (f"Seu depósito inicial foi de R${deposito_inicial:8.2f}, o juros mensais é de {juros:.2f}%, o ganho obtido foi de R${saldo-deposito_inicial: 8.2f} ")
