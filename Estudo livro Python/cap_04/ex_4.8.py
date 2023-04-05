#Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada \
num1 =int(input("Digite o primeiro número inteiro a ser calculado: "))
num2 = int(input("Digite o segundo número inteiro a ser calculado: "))
resultado = ()
operador =  int(input("Escolha qual tipo de cálculo deseja executar\n1 - Multiplicação(*)\n2 - Divisão(/)\n3 - Soma(+)\n4 - Subtração(-)"))

if operador == 1:
    resultado = num1*num2
    print("O resultado do seu cálculo é %d"%(resultado))
elif operador ==2:
    resultado = num1/num2
    print("O resultado do seu cálculo é %d"%(resultado))
elif operador ==3:
    resultado = num1+num2
    print("O resultado do seu cálculo é %d"%(resultado))
elif operador ==4:
    resultado = num1-num2
    print("O resultado do seu cálculo é %d"%(resultado))
else:
    print("É necessário que escolha um operador, para que seja realizado seu cálculo.")
    