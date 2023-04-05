#exemplo de composição de string

nome = "joão"
idade = 23
grana = 109.75

print("%s tem %d anos e R$%f no bolso. " %(nome, idade, grana))
    #joão tem 23 anos e R$109.750000 no bolso.

print("%12s tem %03d anos e R$%5.2f no bolso. " %(nome, idade, grana))
    #        joão tem 023 anos e R$109.75 no bolso. 

print("%12s tem %3d anos e R$%5.2f no bolso. " %(nome, idade, grana))
    #        joão tem  23 anos e R$109.75 no bolso.

print("%-12s tem %-3d anos e R$%-5.2f no bolso. " %(nome, idade, grana))
    #joão         tem 23  anos e R$109.75 no bolso.









