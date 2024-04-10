# Metodos da classe set #

# METODO UNION # SERVE PARA JUNTAR CONJUNTOS MATEMATICOS
# {}.union
# Retorna um valor dos conjuntos juntos 
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_AB = conjunto_a.union(conjunto_b)

print(conjunto_AB)

# METODO INTERSECTION # // Serve para pegar e juntar dois valores iguais.

conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

conjunto_e = conjunto_c.intersection(conjunto_d)

print(conjunto_e)

# METODO DIFFERENCE # / Retorna a diferenca do conjunto que nao esta no outro.


conjunto_f = {1,2,3}
conjunto_g = {2,3,4}

conjunto_h = conjunto_g.difference(conjunto_f)

print(conjunto_h) # {4}

# METODO SYMMETRIC_DIFFERENCE #  // ESSE SIM RETORNA O VALOR DIFERENTE
#(QUE NAO TEM) DENTRE OS 2 CONJUNTOS

conjunto_i = {1,2,3}
conjunto_j = {2,3,4}

conjunto_k = conjunto_i.symmetric_difference(conjunto_j)

print(conjunto_k) # {1, 4}

# METODO ISSUBSET # || retorna um valor booleano indicando se tudo que esta em A se encontra em B
# quase igual um every ou um some de array em js.

conjunto_l = {1,2,3}
conjunto_m = {4,1,2,5,6,3}

conjunto_n = conjunto_l.issubset(conjunto_m)

print(conjunto_n) # True


# METODO ISSUPERSET #  Aqui refere-se se os elementos de B estão em A
# mas se TODOS os elementos de B estao em A, então é um superSET
# Retorna um valor booleano

conjunto_o = {1,2,3}
conjunto_p = {4,1,2,5,6,3}

conjunto_q = conjunto_o.issuperset(conjunto_p) #FALSE

print(conjunto_q) 

# METODO ADD # // metodo para add um novo item.
# Se passasr o mesmo valor que ja existe, ele vai ser ignorado.

sorteio = {1,23}
sorteio.add(25)
sorteio.add(30)
sorteio.add(50)

print(sorteio)

# Metodo clear # // ele limpa o conjunto.

sorteio.clear()


# Metodo Copy # // faz uma cópia do conjunto.

sorteio2 = sorteio.copy()

# Metodo discard # // ele descarta o elemento.

numeros = {2,1,4,6,8}
numeros.discard(6)

print(numeros)

# Metodo pop # Retira o primeiro elemento da lista 
# Retorna o valor tirado.

numeros.pop()

# Operador IN  // verifica se existe um elemento no conjunto e retorna um boolean

possui = 2 in numeros 
naopossui = 3 in numeros
print(possui)
print(naopossui)