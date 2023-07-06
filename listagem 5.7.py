#Imagine que o problema agora seja um pouco diferente: imprimir apenas os números pares entre 0 e um número digitado pelo usuário, de forma bem similar ao problema anterior. Poderíamos resolver o problema com um if para testar se x é par ou ímpar antes de imprimir. Vale lembrar que um número é par quando é 0 ou múltiplo de 2. Quando é múltiplo de 2, temos que o resto da divisão desse número por 2 é 0, ou seja, o resultado é uma divisão exata, sem resto. Em Python, podemos escrever esse teste com x % 2 == 0 (resto da divisão de x por 2 é igual a zero), alterando o programa anterior para o da listagem 5.
fim = int(input("Digite o último número a imprimir:"))
x = 0
while x <= fim:
    if x % 2 ==0:
        print(x)
    x = x+1


#Agora, finalmente, estamos resolvendo o problema, mas poderíamos resolvê-lo de forma ainda mais simples se adicionássemos 2 a x a cada epetição. Isso garantiria que x sempre fosse par. Vejamos o programa da istagem 5.8
fim = int(input("Digite o último número a imprimir:"))
x = 0
while x <= fim:
    x = x+2


#Esses dois exemplos mostram que existe mais de uma solução para o problema, que podemos escrever programas diferentes e obter a mesma olução. Essas soluções podem ser às vezes mais complicadas, às vezes mais imples, mas ainda assim corretas