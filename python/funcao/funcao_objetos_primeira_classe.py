# # # OBJETOS DE PRIMEIRA CLASSE  # #

# Em python tudo é objeto, dessa forma, funcoes também são objetos.
# O que as tornam objetos de primeira classe.

# Com isso, ppodemos atribuir funcoes a variaveis, passa-las como parametro para funcoes,
# usa-las como valores em estruturas de dados:
# (listas, tuplas,dicionarios, etc.)
# E usar como valor de retorno para uma funcao (closures)

def somar (a, b):
       return a + b

def exibir_resultado(a, b, funcao):
       resultado = funcao(a, b)
       print(f"O resultado da operacao {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar) # 20 

# referencia da funcao

op = somar

print(op(2,3))