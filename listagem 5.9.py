#Vejamos outro tipo de problema. Imagine ter que imprimir a tabuada de adição de um número digitado pelo usuário. Essa tabuada deve ser impressa de 1 a 10, sendo n o número digitado pelo usuário. Teríamos, assim, n+1, n+2, ... n+10. Confira a solução na listagem 5.9.

n = int(input("Tabuada de: "))
x = 1
while x <=10:
    print(n+x)
    x = x+1
    
