#exercicio 3.11 Faça um programa que solicite o preço de uma mercadoria e o perccentual de desconto. Exiba o valor do desconto e o preço a pagar
preco_mercadoria = float(input("Qual valor da mercadoria?"))
percentual_desconto =  float(input("Qual percentual de desconto?"))
desconto_total = (preco_mercadoria*percentual_desconto)/100
preco_com_desconto = preco_mercadoria-desconto_total
print("O valor da mercadoria é R$%.2f, o valor do percentual de desconto aplicado é de R$%.2f, o preço atualizado com o desconto aplicado é de R$%.2f"%(preco_mercadoria, desconto_total, preco_com_desconto))