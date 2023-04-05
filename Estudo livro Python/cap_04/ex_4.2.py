#Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de m usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h   \

#perguntar a velocidade ao usuario
velocidade = float(input("Qual a velocidade está trafegando com seu veículo? :\n "))

#condição do limite de velocidade
if velocidade>80:
    print("Você foi multado por excesso de velocidade")
elif velocidade <= 80:
    print("Boa viagem!")

#condição para aplicação de multa se necessário

if velocidade > 80:
#variável contadora para contabilizar o saldo da multa
    multa = (velocidade-80)*5
    print("sua multa é no valor de R$%d "%(multa))


    