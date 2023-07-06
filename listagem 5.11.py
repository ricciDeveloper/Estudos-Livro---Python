#O programa começa inicializando a variável "n" com o valor 1. Essa variável será utilizada como um contador, para controlar o número de iterações do loop.
#contador
n = 1


# a variável "soma" é inicializada com o valor 0. Essa variável será utilizada como um acumulador, para armazenar a soma dos valores digitados pelo usuário.
#acumulador
soma = 0


#O loop while é iniciado com a condição "n <= 10", ou seja, o loop irá se repetir enquanto o valor de "n" for menor ou igual a 10. 
while n <= 10:

    #é solicitado que o usuário digite um número, que é armazenado na variável "x".
    x = int(input("Digite o %d número: "%n))
    
    
    # o valor de "x" é adicionado ao valor atual da variável "soma", utilizando o operador de soma (+).
    soma = soma + x
  
  
   #o valor de "n" é incrementado em uma unidade, utilizando o operador de soma (+1).
    n = n +1


    #Após o término do loop, o programa imprime o valor da variável "soma", utilizando o método "print" e formatação de string.
print("soma: %d"%soma)
