#  # ARGS E KWARGS #

# Podemos combinar parametros obrigatorios com args e kwargs.
# Quando esses sao definidos (*args e **kwargs)
# o metodo recebe os valore s como tupla e dicionario respectivamente

# (*args) -> valores vindo dentro de uma tupla ("dados")
# (**kwargs) -> valores vindo como um dicionario ({"dados": {"id": "1"}})

# EXEMPLO #

def exibir_poema(data_extenso, *args, **kwargs):
       texto = "\n".join(args)
       meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
       mensagem = f"{data_extenso}\n\n{meta_dados}"
       print(mensagem)

exibir_poema("Quinta feira, 11 de abril, 2024","Zen of Python", "Beautiful is better than ungly.", autor="Tim Peters", ano=1999)