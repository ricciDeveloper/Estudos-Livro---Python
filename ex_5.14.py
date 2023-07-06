#Exercício 5.14 Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética \


num_digitados = 0
media = 0 
contador = 0
soma = 0 
while True:
    number = int(input("Digite os valores a serem somados\n ============ 0 para sair ================\n"))
    num_digitados = num_digitados + number
    soma = soma+1
    if number == 0:
        print (f"A soma dos números digitados foi: {num_digitados}\nA média aritmética dos números foi: {media}\nFoi digitado {soma-1} números durante o programa  ")
        break
        
        
    contador = number
    media = num_digitados/contador
    