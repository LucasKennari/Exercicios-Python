# # METODO CLEAR # # // Ele limpa o dicionario.
contatos = {
       "guilherme@email.com": {"nome": "Guilherme", "telefone": "31234415"},
       "lucas@email.com": {"nome": "lucas", "telefone": "4214145"},
       "abc@email.com": {"nome": "abc", "telefone": "12415"},
}
# {}.clear

contatos.clear()

print(contatos) #{}

# # METODO COPY # # 
# // faz uma copia do dicionario

contatos = {
       "guilherme@email.com": {"nome": "Guilherme", "telefone": "31234415"},
       "lucas@email.com": {"nome": "lucas", "telefone": "4214145"},
       "abc@email.com": {"nome": "abc", "telefone": "12415"},
}
copia = contatos.copy()
copia["guilherme@email.com"] = {"nome":"Gui"}
contatos["guilherme@email.com"]

print(copia["guilherme@email.com"])
print(contatos["guilherme@email.com"])

# # METODO FROMKEYS # #
# // ele cria chaves
# 1 situacao, quando vc quer criar chave e só deixar la, sem valor.
# ele vai criar com valor none

dados = dict.fromkeys(["nome", "telefone"]) 
# dados: {'nome': None, 'telefone': None}
print("dados:", dados)

# 2 situacao vc quer criar um conjunto de chaves e deixar com valor padrao

dados2 = dict.fromkeys(["nome", "telefone"], "vazio")
#dados2 {'nome': 'vazio', 'telefone': 'vazio'}
print("dados2", dados2)

# # METODO GEET # #
contato = {
        "guilherme@email.com": {"nome": "Guilherme", "telefone": "31234415"},
}

# contato["chaves"] # keyErro

contato.get("chave") # None // se ele nao encontrar a chave, ele retorna none.

contato.get("chave", {}) # {} // é possivel retornar um valor default como segundo argumento

contato.get("guilherme@email.com", {}) # retorna toda a chave com o valor.

# # METODO ITEMS # # 

contatin = {
       "id": 2,
        "guilherme@email.com": {"nome": "Guilherme", "telefone": "31234415"},
}

resultado = contatin.items() # retorna uma lista de tuplas

# print(resultado)

# # METODOS KEYS # #
# retorna só as chaves

print(contatin.keys()) # // dict_keys(['guilherme@email.com'])


# # METODO POP # #
# Remove o valor

metodo_pop = contatin.pop("id")
metodo_pop = contatin.pop("id", {}) # se nao tiver o valor, retorna um valor default
print(metodo_pop) # retorna o valor que foi tirado.
print(contatin)

# # Metodo popitem # # 
# / Igual o pop, mas nao é preciso informar a chave.
# ele tira item na sequencia
# se nao tiver mais chaves, ele vai dar keyError

# # Metodo SETDEFAULT # #
# se nao tiver o valor dentro do dicionario, ele coloca um valor padrao

# se possuir, ele retorna o valor dentro e nao substitui

# Ex1 com valores ja existentes:
dado0 = {"nome":"lucas", "idade": 134}

dado0.setdefault("nome", "robverto")

print(dado0) # retorna os valores sem estarem modificados 
# pois as chaves ja existem

# EX2 sem valores existentes:

dado0.setdefault("telefone","2222-2222")

print(dado0) # retorna os valores modificado com a chave que nao existe

# # METODO UPDATE # # 
# Ele atualiza o dicionario
pessoas = {"pessoa": {"nome": "lucas"}}
# ex 1
pessoas.update({"pessoa": {"nome": "lucas kennari"}}) # atualiza o dicionario

# ex 2
pessoas.update({"pessoas": {"nome": "kennari"}}) # ele adiciona um nova chave
print(pessoas)

# # METODO VALUES # #

# keys retorna todas as chaves de nome unico ex: "id", "nome", etc..
# ja os valores, retorna todos os valores dentro das chaves
print(pessoas.values())

# # Metodo IN # #
# verifica se aquela chave está dentro do dicionario
# e retorna um valor oboleano

possui_A_chave = "pessoa" in pessoas
retorna_false_se_nao_tiver_a_chave = "telefone" in pessoas

print(possui_A_chave) # true
print(retorna_false_se_nao_tiver_a_chave) # false