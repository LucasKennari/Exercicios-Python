# # Argumentos nomeados
# Funcoes também podem ser chamadas usando argumentos de forma
# chave = valor


def salvar_carro(marca, modelo, ano, placa):
       print(f"Carro inserido com sucesso ! {marca}/{modelo}/{ano}/{placa}")


# salvar_carro("fiat","Palio", 1999, "ABC-1234") # 1 opcao
# salvar_carro(marca="fiat",modelo="Palio", ano=1999, placa="ABC-1234")  # 2 opcao
salvar_carro(**{"marca":"fiat", "modelo": "Palio", "ano": "1999", "placa": "123-345" })  # 3 opcao

# Apesar da primeira funcionar, de forma escalavel ela pode acabar dando erro se alguém esquecer
# se passar algum argumento ou acabar invertendo.

# A mesma coisa se vale para a segunda opcao, podem acabar invertendo a ordem ou mudando os arg

# Ja a terceira opcao, com os asteristicos "**{}" está informando um dicionario