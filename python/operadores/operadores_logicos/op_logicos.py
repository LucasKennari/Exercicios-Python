# Operadores lógicos: 
# São operadores utilizados em conjunto com os operadores de comparacao
# para montar uma expressão lógica. Quando um operadorde comparacao é utilizado
# o resultado retornado é um boolean, desta forma poidemos combinar operadores de comparacao
# com os operadores lógicos

# # # op_comparacao + op_logico + op_comparacao ...

# # Ex:
saldo = 1000
saque = 200
limite = 100

# # print(saldo >= saque)

# # print(saque <= limite)

# # # Operador E (and)
# o operador AND retorna TRUE se ambas as partes forem VERDADEIRAS
# print(saldo >= saque and saque <= limite) # v / f = falso


# Operador OU (or)
# # retorna TRUE se apenas UMA das condicoes for VERDADEIRA
#print(saldo >= saque or saque <= limite) # v / f = TRUE

# Operador de NEGACAO (not)

contatos_emergencias = []

print(not 1000 > 1500)

print(not contatos_emergencias)

print(not "saque 1500")

print(not "")