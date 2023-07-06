pontos = 0 
questao = 1

while questao <= 3:
    resposta = input("Resposta da questão %d: "%(questao))
    if questao == 1 and (resposta =="B" or resposta =="b"):
        pontos = pontos+1
    elif questao ==2 and (resposta =="A" or resposta =="a"):
        pontos = pontos+1
    elif questao == 3 and (resposta =="c" or resposta =="C"):
        pontos = pontos+1
    questao +=1
print("O aluno fez %d ponto(s)"%pontos)