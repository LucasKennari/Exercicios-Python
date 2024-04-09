# # Vamos entender o funcionamento da estrutura de dados tupla.

# # # Oque é tupla?

# Tuplas são estruturas de dados muito parecida com as listas,
# a principal diferenca é que tuplas são IMUTAVEIS. enquanto listas 
# são mutaveis. Podemos criar tuplas através da classe tuple, ou
# colocaando valores separados por virgula de parenteses

# Ex:
frutas = ("laranaja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1,2,3,4])
pais = ("brasil",)

print(frutas)
print(letras)

# Acesso direto

# A tupla é uma sequencia,a portanto podemos acessar seus dados utilizando
# indices. Contamos o indice de determinada sequencia a partir do zero

# Acessando o indice.
print(letras[5])

# Indice negativo
print(letras[:: -1])

# Tuplas aninhadas

# Tuplas podem armazenar todos os tipos de objetos Python,
# portanto podemos ter tuplas que armazenam outras tuplas.
# Com isso podemos criar estrutura bidimensionais, vulgo tabelas.


matriz = (
(1, "a", "2"),
("b", 3, 4),
(5, 6, "c"),
)

# também existe o fatiamento na tupla
#tambem tem for.

# Metodos da classe tuple

# ().count // conta quantos elementos repetidos tem dentro
# ().indice // mostra valor do indice de onde está o elemento passado como argumento
# len() // conta quantos elementos tem dentro da tupla.

