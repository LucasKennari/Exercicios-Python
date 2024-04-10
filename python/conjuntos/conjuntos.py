# objetivo :
# Entender o funcionamento da estrutura de dados set

# Oque é conjuntos:
# Um set é uma colecao que nao possui objetos repetidos, usamos sets para 
# representar conjuntos matematicos ou eliminar itens duplicados de um
# iteravel

# Ex 1
exemplo1 = set([1,2,3,1,3,4])
exemplo2 = set("abacaxi")
exemplo3 = set({2,5,7,9,4,2,4,6,7})
exemplo4 = {"python", "java", "python"}
set("abacaxi")

print(exemplo1)
print(exemplo2)
print(exemplo3)
print(exemplo4)

# # Acessando os dadoss

# Conjuntos em python nao suportam indexacao e nem fatiamento,
# caso queira acessar os seus valores é necessário CONVERTER o 
# conjunto para listar

conjt = {1 , 2 , 3 ,4}
arr = list(conjt)

print(arr[0])

# # ITERAR CONJUNTOS #

# é possivel percorrer o set utilizando for

carros = {"gol", "celta", "palio"}

for carro in carros:
       print(carro)

# # ENUMERATE # 

# Às vezes é necessário saber qual o indice do objeto dentro do laco for.
# Para isso podemos utilizar a funcao enumerate

nomes = {"paulo", "roberto", "lucas"}

for index, nome in enumerate(nomes):
       print(f"{index} : {nome}")

