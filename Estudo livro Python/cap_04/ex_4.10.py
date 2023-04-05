#Exercício 4.10 Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios

consumo_kwh = float(input("Qual seu consumo em kW/h?\n"))
tipo_instalação = int(input("Qual o tipo de instalação do local?\n1 - Residencial\n2 - Comercial\n3 - Industrial\n"))

preco_kwh = ()
preco_final = ()

if tipo_instalação ==1 and consumo_kwh<=500:
    preco_kwh =  consumo_kwh*0.40
    print("O preço da sua conta de energia, referente ao seu consumo é de R$%6.2f" %(preco_kwh))
elif tipo_instalação==1 and consumo_kwh>500:
    preco_kwh =  consumo_kwh*0.65
    print("O preço da sua conta de energia, referente ao seu consumo é de R$%6.2f" %(preco_kwh))
elif tipo_instalação ==2 and consumo_kwh<=1000:
    preco_kwh =  consumo_kwh*0.55
    print("O preço da sua conta de energia, referente ao seu consumo é de R$%6.2f" %(preco_kwh))
elif tipo_instalação ==2 and consumo_kwh>1000:
    preco_kwh =  consumo_kwh*0.60
    print("O preço da sua conta de energia, referente ao seu consumo é de R$%6.2f" %(preco_kwh))
elif tipo_instalação ==3 and consumo_kwh<=5000:
    preco_kwh =  consumo_kwh*0.55
    print("O preço da sua conta de energia, referente ao seu consumo é de R$%6.2f" %(preco_kwh))
elif tipo_instalação ==3 and consumo_kwh>5000:
    preco_kwh =  consumo_kwh*0.60
    print("O preço da sua conta de energia, referente ao seu consumo é de R$%6.2f" %(preco_kwh))
