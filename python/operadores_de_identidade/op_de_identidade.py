# # O que é:
# São operadores utilizados para comparar se os dois objetos testados
# ocupam a mesma posicao na memória


# O operador de identidade é o IS, para comparar se o obj A 
# ocupa a mesma memoria que o obj B, Utilizamos o IS
curso = "curso de python"
nome_curso = curso
saldo, limite = 200, 200
print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)