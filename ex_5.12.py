#Exercício 5.12 Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.



deposito_inicial = float(input("Qual déposito incial: "))
juros = float(input("Qual juros mensais da poupança: "))

deposito_mensal_recorrente = float(input("Qual déposito mensal recorrente: "))

saldo = deposito_inicial 
meses = 0


while meses <=24:
    
    saldo = saldo + (saldo *(juros/100)) + deposito_mensal_recorrente
    
    print(f"Saldo do mês {meses} é de R${saldo:5.2f}.")
    meses = meses+1


print (f"Seu depósito inicial foi de R${deposito_inicial:8.2f}, o juros mensais é de {juros:.2f}%, o ganho obtido foi de R${saldo-deposito_inicial-deposito_mensal_recorrente: 8.2f}, seu depósito mensal recorrente além do inicial foi de R${deposito_mensal_recorrente: 8.2f} ao mês, totalizando o valor em R${deposito_mensal_recorrente*(meses-1):8.2f} ")