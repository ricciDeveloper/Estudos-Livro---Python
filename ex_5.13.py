#Exercício 5.13 Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago  \


#perguntamos ao usuário, o valor da dívida, a taxa de juros, e o valor mensal a ser pago
divida = float(input("Qual valor da divida: \n"))
taxa = float(input("Qual a taxa de juros: (exemplo, 2 para 2%)\n"))
pagamento = float(input("Qual valor do pagamento mensal que será executado: \n"))

#varial contadora, para somar os meses de pagamento
meses = 0

#variável criada para armazenar o juros total, a cada loop do while
juros_total = 0

#váriavel criada para ser atribuido o valor devedor, retirando o pago, e somado ao juros
saldo_devedor = divida


#loop de repetição a ser executado enquanto houver saldo devedor
while saldo_devedor > 0:
    #calculo do juros
    juros = saldo_devedor * (taxa/100)
    #atribuição do juros a váriavel para acumlar o valor em juros
    juros_total += juros

    #variavel para atribuir e guardar o saldo devedor, somado ao juros, subtraido aos pagamentos
    saldo_devedor +=juros - pagamento

    #incrementação de mes a mes, para saber quantos meses levará para quitar a divida
    meses += 1 
#impressão na tela das váriaveis, feito por formtação de string - f""
print (f"Levou {meses} meses para quitar a divida \nO total pago foi de R${pagamento*meses:.2f}\nO total de juros pago foi de R${juros_total:.2f}")

