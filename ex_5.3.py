#Exercício 5.3 Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.
contagem = 10
while contagem <=10 and contagem>=0:
    print("%s segundos para o lançamento do foguete" %(contagem))
    contagem = contagem-1