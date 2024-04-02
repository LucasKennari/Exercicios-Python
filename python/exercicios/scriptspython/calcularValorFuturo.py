valorPresente = float(input("Digite o valor presente: \n"))
taxaDeJuros = float(input("Digite a taxa de juros anual: \n"))
tempo = float(input("Digite o tempo em anos: \n"))

ValorFuturo = round(float(valorPresente * ( 1 + taxaDeJuros)**tempo),2)

print(f"Valor ao ano durante {tempo} anos equivale a {ValorFuturo}" )