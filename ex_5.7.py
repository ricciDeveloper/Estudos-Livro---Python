#Exercício 5.7 Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10
n = int(input("Digite o início da tabuada: "))

fim = int(input("Digite o fim da tabuada"))


while n <= fim:
    resultado = n*fim
    print(f"{n} X {fim} = {resultado}")
    n = n+1