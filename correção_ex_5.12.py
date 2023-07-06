
# Ele começa pedindo três valores de entrada do usuário: o depósito inicial, a taxa de juros e o valor do depósito mensal.
depósito = float(input("Depósito inicial: "))


taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
investimento = float(input("Depósito mensal: "))

#o código inicializa algumas variáveis, como mes(que representa o mês atual) e saldo(que representa o saldo da conta). O saldo inicial é definido como o depósito inicial informado pelo usuário.

mês = 1
saldo = depósito

# entra em um loop que executa 24 vezes, uma vez para cada mês do período em questão. Dentro do loop, ele calcula o novo saldo da conta, adicionando os juros do mês anterior ao saldo atual, multiplicado pela taxa de juros incidente pelo usuário, e adicionando também o valor do depósito mensal garantido pelo usuário.
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
    mês = mês + 1

    #o código calcula o ganho obtido com os juros, subtraindo o depósito inicial do saldo final da conta. Esse valor é impresso na tela.
print(f"O ganho obtido com os juros foi de R${saldo-depósito:8.2f}.")