#Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem \
velocidade_media = float(input('Qual velocidade média prevista para o percurso?\n '))
distancia_destino = float(input('Qual a distância em Km do destino?\n'))

tempo_viagem = distancia_destino / velocidade_media
print("O tempo estimado de sua viagem é de %.2f horas"%(tempo_viagem))