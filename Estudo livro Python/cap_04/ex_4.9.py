#Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar

#perguntas ao usuário
valor_casa = float(input("Qual o valor do imóvel a ser adquirido?"))
salario = float(input("Qual seu salário atual?"))
anos_pagamento = int(input("Em quantos anos deseja pagar o imóvel?"))

#armazenar informaçoes

        #meses ao todo do pagamento
meses_totais_pagamento = anos_pagamento*12
        #Calculo do limite de valor mensal, estipulado em 30%
    
limite_mensalidade = (salario*0.30)
        #calculo para ponderar o valor da mensalidade
mensalidade_imóvel = valor_casa/meses_totais_pagamento

#condições
if mensalidade_imóvel<=limite_mensalidade:
    print("Você adquiriu seu empréstimo, com o valor mensal de R$%6.2f, por %d meses, e %d anos."%(mensalidade_imóvel, meses_totais_pagamento, anos_pagamento ))
elif mensalidade_imóvel>limite_mensalidade:
    print("Não podemos conceder uma parcela mensal que exceda 30%, do valor mensal do seu salário.")
else:
    print("É necessário preencher os campos corretamente para concluir esta simulação de empréstimo.   ")
    