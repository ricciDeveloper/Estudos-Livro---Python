#Exercício 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período 



#Ele começa pedindo dois valores de entrada do usuário: o depósito inicial e a taxa de juros.
depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))


#ele inicializa algumas variáveis, como mes(que representa o mês atual) e saldo(que representa o saldo da conta). O saldo inicial é definido como o depósito inicial informado pelo usuário.
mês = 1
saldo = depósito


#loop que executa 24 vezes, uma vez para cada mês do período em questão
while mês <= 24:

    #Dentro do loop, ele calcula o novo saldo da conta, adicionando os juros do mês anterior ao saldo atual, multiplicado pela taxa de juros pelo usuário.
    saldo = saldo + (saldo * (taxa / 100))

    #O saldo atualizado é então impresso na tela, juntamente com o número do mês correspondente. O loop continua até que o mês atual chegue a 24.
    print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
    mês = mês + 1

    #o código calcula o ganho obtido com os juros, subtraindo o depósito inicial do saldo final da conta. Esse valor é impresso na tela.
print(f"O ganho obtido com os juros foi de R${saldo-depósito:8.2f}.")