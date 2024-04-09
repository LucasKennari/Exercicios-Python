# Metodos de array

## Metodo append()
[].append #equivalente ao arr.push(valor)
# # Ex
lista = []
lista.append(1)
lista.append("Python")
lista.append([40,30,50])

print(lista) # // [1, 'Python', [40, 30, 50]]

# # Metodo clear // Utilizado para limpar a array
[].clear()

lista2 = [[1, 'Python', [40, 30, 50]]]
print(lista2)

lista2.clear()
print(lista2)

# # metodo copy // garante a copia dos mesmos valores sem afetar a lista.

[].copy
l2  = lista.copy()

# # Metodo count // conta quantas vezes um determinado objeto aparece na lista

# [].count()

cores = ["vermelho" , "azul", "verde" , "azul"]
vermelho = cores.count("vermelho")
azul =  cores.count("azul")

print("vermelho" , vermelho, "azul:", azul)

# # Metodo extend // Funciona pra juntar um ou mais elementos com outra lista
# também podendo juntar com outro array.
# ele nao junta valores duplicados.

# [].extend()

linguagens = ["python", "js" , "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])

linguagens2 = linguagens.copy()

print(linguagens)

# # Metodo index // saber qual indice que se encontra o elemento

# [].index()

indexJava = linguagens.index("java")
indexCsharp = linguagens.index("csharp")

print(indexJava, indexCsharp)

# Ele nao retorna todas as ocorrencias, só retorna a primeira.


# # Metodo Pop // Remove o ultimo elemento, mas é possivel 
# informar o indice que deseja remover
# ele retorna o valor que foi tirado.
# [].pop

ultimo_elemento = linguagens.pop()
primeiro_elemento = linguagens.pop(0)

print(primeiro_elemento)
print(ultimo_elemento)

print(linguagens)

# # Metodo remove // segunda forma de remover um elemento da lista
# diferente do POP, ao inves de passar um indice, vc pode passar
# o valor/nome do elemento.
# ele nao retorna nenhum valor.
# ele tira apenas uma ocorrencia de c, ou seja, a primeira.
# [].remove()

remover_C = linguagens.remove("c")

print(remover_C)
print(linguagens)

# # Metodo reverse // inverte os elementos.

lista_par =[2 , 4,6,8,10]
lista_par.reverse()

print(lista_par)

# # Metodo sorte // Ordena a lista
linguagens2.sort() # // Ordena alfabeticamente
linguagens2.sort(reverse=True) # // ordena em ordem alfabetica, mas espelhado.
linguagens2.sort(key=lambda x: len(x)) # // ordena na ordem crescente de acordo com quantos caracteres tem cada palavra
linguagens2.sort(key=lambda x: len(x), reverse=True) # // ordena de ordem decrescente

print(linguagens2)

# # Metodo len // Funciona igual o length, diz qual o tamanho do array

print(len(linguagens2))


# # Metodo sorted // funcao builting funciona como sort

# sorted(1 argumento é o array: 2 argumento: funcao anonima: 3 argumento é o tamanho)


