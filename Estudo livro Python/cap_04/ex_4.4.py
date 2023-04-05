#Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

#pergunta ao usuário o valor do salário para o calculo
salario = float(input("Digite seu salário: \n"))

#variavel para salvar o salário, sem que o valor seja alterado 
base = salario

#variavel para ser atribuido o valor do cálculo de aumento, baseado no salario
aumento = 0
#condição lógica para calculo do aumento do salario
if base>1250:
    aumento = (base*0.10)
    salario_atualizado = base+aumento
    print(salario_atualizado)
if base<=1250:
    aumento = (base*0.15)
    salario_atualizado = base+aumento
    print(salario_atualizado)