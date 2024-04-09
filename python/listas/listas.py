# # Criando istas

# lista em Python podem armazenar de maneira sequencial qualquer tipo de objeto.
# Podemos criar listas utilizand o construtor list. 
# a funcao RANGE ou colocando valores separados por virgula dentro de colchetes
# listas são objetos mutáveis, portanto podemos alterar seus vallores após a criacao

# # Criando com construtor list:
letras = list("python") 
# print(letras)
# // Ele nao cria uma lista chamada python
# e nem coloca a letra python dentro de um array.
# ele separa cada caractere em um indice dentro de uma array.
# igual o split()

numeros = list(range(10)) # Cria uma lista de 0 a 9
# # print(numeros)

# # Lista com colchetes
 
frutas = ["laranja", "maca", "uva"]
furtas = []

carro = ["ferrari", "f8", 40000, True]

# # Acesso direto:

# A lista é uma sequencia, portanto podemos acessar seus dados utilizando
# indices. Contamos o indice de determinada sequencia apartir do zero

# # 1* elemento

frutas[0] # laranja.

# # Indices negativos : 
# sequencia suportam indexacao negativa. A contagem comeca em -1

frutas[-1] # Uva // -1 é o ultimo elemento da lista.

# # Listas aninhadas 

# Listas podem armazenar TODOS os tipos de objetos em Python,
# portanto podemos ter listas que armazenam outras listas.
# com isso podemos criar estruturas bidimensionais (tabelas),
# e acessar informando os indices de linha e coluna.

matriz = [
       [1, "a", 2],
       ["b",3, 4],
       [6, 5, "c"],
]
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])


# # Fatiamento:

# Além de acessar elementos diretamente, podemos extrair um conjunto de valores
# de uma sequencia. Para isso basta passar o indice inicial
# e/ou final para acessar o conjunto. Podemos ainda informar
# quantas posicoes o cursosr deve pular no acesso

arr = list("fatiamento")

fatiamento1 = arr[2:] # t i a m e n t o
fatiamento2 = arr[:2] # f a
fatiamento3 = arr[0:-1:2] # f t a e t
fatiamento4 = arr[:: -1] # 'o', 't', 'n', 'e', 'm', 'a', 'i', 't', 'a', 'f'
fatiamento5 = arr[::] # retorna uma cópia da arr

# print(fatiamento2)
# print(fatiamento3)
# print(fatiamento4)

# ITERAR LISTAS #

# A forma mais comum para percorrer os dados
# de uma lista é utilizando o comando FOR.

carros = ["gol", "celta", "palio"]
# for carro in carros:
#        print(carro)

# FUNCAO ENUMERATE #
# as vezes é necessário saber qual o indice do objeto dentro do laco for
# para isso podemos usar a funcao ENUMERATE

for indice, carro in enumerate(carros):
       print(f"{indice}: {carro}") 
# 0: gol  
# 1: celta
# 2: palio

# COMPREENSAO DE LISTAS #

# A compreensao de lista oferece uma sintaxe mais curta quando voce deseja
# criar uma nova lista com base nos valores de uma lista existente(filtro)
# ou gerar uma nova lista aplicando alguma modificacao nos elementos de uma lista existentes

# basicamente voce aplicar certas condicoes pra aquela array retornar o valor que vc quer
# exemplo: retornar uma lista de numeros maior que 18

# FILTRO EX 1: #

numeros = [1, 30, 31, 31, 2, 9, 65, 34]
pares = []

for numero in numeros:
       if numero % 2 == 0:
              pares.append(numero)

# COMPREENSAO: FILTRO EX 2 #

numeros2 = [1, 30, 31, 31, 2, 9, 65, 34]
pares2 = [numero for numero in numeros2 if numero % 2 == 0]
quadrado = [numero ** 2 for numero in numeros2] 

print(pares2)
