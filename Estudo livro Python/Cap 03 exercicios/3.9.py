#Exercício 3.9 escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos. \
dias = int(input("Digite a quantidade de dias que deseja calcular em segundos: "))
horas = int(input("Digite a quantidade de horas que deseja calcular em segundos: "))
minutos = int(input("Digite a quantidade de minutos que deseja calcular em segundos: "))
segundos = int(input("Digite a quantidade de segundos que deseja somar ao calculo do dia em segundos: "))
dias_seg = dias*86400
horas_seg = horas*3600
minutos_seg = minutos*60
segundos_totais = dias_seg + horas_seg + minutos_seg + segundos

print("O total de dias em segundos é de: %d segundos\no total de horas em segundos é de %d\no total de minutos em segundos é de: %d,\ne o total de segundos da data informada para o calculo(incluso os segundos informados por você usuário) é de: %d" %(dias_seg, horas_seg, minutos_seg, segundos_totais))