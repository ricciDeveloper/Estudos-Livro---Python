#Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário
salario_atual = float(input("Digite seu salário atual"))
aumento_porcentagem = int(input("Digite qual percentual de aumento do seu salário"))
salario_aumento = (float((salario_atual * aumento_porcentagem)/100))
print("O valor de reajuste do seu salário é de:           %.2f"%(salario_aumento))
print("Seu salário total agora é de:    %.2f" %(salario_aumento+salario_atual))