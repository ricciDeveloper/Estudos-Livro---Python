#Exercício 4.3 Escreva um programa que leia três números e que imprima o maior e o menor.
number1 = int(input("Digite o primeiro número : \n"))
number2 = int(input("Digite o segundo número : \n"))
number3 = int(input("Digite o segundo número : \n"))

if number1>number2 and number1>number3:
    print("O maior dos numéros é\n %d "%(number1))
if number2>number1 and number2>number3:
    print("O maior dos numéros é \n%d "%(number2))
if number3>number1 and number3>number2:
    print("O maior dos numéros é\n%d " %(number3))

if number1==number2 or number1==number3 or number2==number1 or number2==number3 or number3==number1 or number3==number2:
    print("Existem igualdades entre um dos valores fornecdios ao sistema")