# conhecer metodos uteis para manipular objetos do tipo string,
# como interpolar valores de variáveis e entender como funciona o fatiamento

#Exemplo 1 //

curso = "pYtHon"

print(curso.upper()) # // Deixa EM CAPS LOCK

print(curso.lower()) # // deixa tudo minusculo

print(curso.title()) # // deixa a primeira letra Maiuscula



#Exemplo 2 // Eliminando os espacos

curso2 = "     Python      "

print(curso2.strip()) # // Funciona igual o trim, elimina os espacos em branco.

print(curso2.lstrip()) # // Elimina os espacos em branco do comeco // Left strip

print(curso2.rstrip()) # // Elimina os espacos em branco do final // Right strip


# Exemplo 3 // Juncoes e centrallizacao.

curso3 = "Python"

print(curso3.center(10, "#")) # preenchera o espaco com 10 caracteres de acordo q for passado. 
#e ele contarar com o total de caracteres dentro da variavel

print(".".join(curso3)) # Ele funciona como um for, vai pecorrendo a string e adicionando 
#o caractere indicado // ele é comum elm listas


