#Exercício 5.9 Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20

#O programa começa pedindo ao usuário que digite o dividendo e o divisor, armazenando esses valores em duas variáveis ​​distintas.
dividendo = int(input("Digite o dividendo :"))
divisor = int(input("Digite o divisor :"))


#, a variável "quociente" é iniciada com o valor zero. Essa variável irá armazenar o resultado da divisão inteira, ou seja, a quantidade de vezes que é possível subtrair o divisor do dividendo, sem resultar em um número negativo.
quociente = 0

#A variável "op" é inicializada com o valor do dividendo. Essa variável será utilizada para armazenar o valor atual do dividendo durante a conclusão da divisão inteira.
op = dividendo


#O próximo passo é um loop "while", que irá repetir que o valor de "x" até seja menor do que o valor do divisor. Dentro do loop, é subtraído o valor do divisor de "x" e, em seguida, o valor de "quociente" é incrementado em uma unidade. Essa operação é repetida até que não seja mais possível subtrair o divisor do valor atual de "x".
while op >= divisor:
    op = op-divisor
    quociente = quociente + 1


#a variável "resto" é atribuída com o valor atual de "op". Essa variável armazena o valor do resto da divisão inteira.
restante  = op


#o programa imprime o resultado da divisão inteira e do resto, utilizando o método "print" do Python e formatação de string.
print("%d / %d = %d(quociente) %d(resto)" %(dividendo, divisor, quociente, restante ))
