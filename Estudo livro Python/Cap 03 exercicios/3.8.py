#Exercício 3.8 Escreva um programa que leia um valor em metros e o exiba convertido em milímetro
largura = int(input("digite a largura em metros: "))
profundidade = int(input("digite a profundidade em metros: "))

largura_mm = largura*1000
profundidade_mm = profundidade*1000

print("A largura em metros é de %d" %(largura))
print("A pronfudidade em metros é de %2d" %(profundidade))
print("A largura em milimetros é de %dmm" %(largura_mm))
print("A pronfudidade em milimetros é de %dmm" %(profundidade_mm))