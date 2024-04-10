# Criando dicionarios

# Um dicionario é um conjunto não-ordenado de pares chave:valor, onde as chaves
# são unicas em uma dada instancia do dicionadio. 
# Dicionários sao delimitados
# por chaves {}, contém uma lista de pares chave:valor separados por virgulas
# OU SEJA, objeto em javascript

# a chave tem q ser um valor IMUTAVEL

pessoa = {"nome": "guilherme", "idade": 27}

pessoa2 = dict(nom="Guilherme", idade=27)

pessoa["telefone"] = "3264543266"
print(pessoa)

print(pessoa["idade"])

dados = {}

dados["nome"] = "Lucas"
dados["idade"] = 28

print(dados)
print(dados["idade"])


# # Dicionarios aninhados # #

# Dicionários podem armazenar qualquer tipo de objeto python como valor,
# desde que a chave para esse valor seja um objeto imutavel como 
# (strings e numeros)

contatos = {
       "guilherme@email.com": {"nome": "Guilherme", "telefone": "31234415"},
       "lucas@email.com": {"nome": "lucas", "telefone": "4214145"},
       "abc@email.com": {"nome": "abc", "telefone": "12415"},
}

# print(contatos["lucas@email.com"])
# print(contatos["guilherme@email.com"]["nome"])

# # Iterar dicionários #

# o for
# A forma mais comum para percorrer os dados de um dicionario é utilizando

# for chave in contatos:
#        print(chave, contatos[chave]) // ele só retorna a chave

for chave, valor in contatos.items():
        print(chave)

# Items retorna uma lista de tuplas,
# o primeiro arg é a chave, e o segundo é o valor

# se no dicionario tiver a chave que esta tentando criar e atribuir, esse valor
#dentro do dicionario vai ser substituido
