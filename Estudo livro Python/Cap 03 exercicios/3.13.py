#Exercício 3.13 Escreva um programa que converta uma temperatura digitada em °C em °F. Formula: F=(9.C/5)+32
graus_celsius = float(input("Qual temperatura em Celsius, deseja converter para graus fahrenheit:"))
graus_fahrenheit = (9*graus_celsius/5)+32
print("A conversão de %.1fºC, para Fahrenheit é: %.1fºF"%(graus_celsius, graus_fahrenheit))