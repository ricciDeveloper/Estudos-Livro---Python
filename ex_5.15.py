#Exercício 5.15 Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:
#Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro “Código inválido”
#tabela: 1 - R$0,50 / 2 - R$1,00 / 3 - R$4,00 / 5 - R$7,00 / 9 - R$8,00
produtos = ("1 - R$0,50 / 2 - R$1,00 / 3 - R$4,00 / 5 - R$7,00 / 9 - R$8,00, digite 0 para fechar a sua conta")
print(f"Os códigos dos produtos, e seus respectivos valores ({produtos})")
saldo_aberto = 0 
while True:
    
    codigo_produto = int(input("Digite o código do prooduto: "))
    preço = 0
    if codigo_produto == 0:
        break
    elif codigo_produto == 1:
        preço = 0.50
        print("Preço do produto escolhido é R$0,50")
    elif codigo_produto == 2:
        preço = 1.00
        print("Preço do produto escolhido é R$1,00")
    elif codigo_produto == 3:
        preço = 4.00
        print("Preço do produto escolhido é R$4,00  ")
    elif codigo_produto == 5:
        preço = 7.00
        print("Preço do produto escolhido é R$7,00")
    elif codigo_produto == 9:
        preço = 8.00
        print("Preço do produto escolhido é R$8,00")
    else:
        print("Código Inválido")
    quantidade = int(input("Digite a qauntidade de produtos: "))
    saldo_aberto = saldo_aberto + (preço*quantidade)
print(f"Total a pagar R${saldo_aberto: 5.2f}")