# # # O QUE SÃO FUNCOES # #

# funcao é um bloco de código identificado por um nome e pode receber uma listaa
# de parametros.
# Esses parametros podem ou não ter valores padrões. 
# Usar funcoes torna o código mais legivel e possibilita o reaproveitamento de código.
# Programaar baseado em funcoes, é o mesmo que dizer que estamos programando
# de maneira estruturada


# def + identificador ():

def exibir_mensagem():
       print("Olá world")


exibir_mensagem()

def exibir_mensagem_nome(nome):
       print(f"Seja bem vindo {nome}!")

exibir_mensagem_nome("lUCAS") # Se eu coloco um argumento sem nenhum vlaor, é obnrigado possuir um arg na funcao

def exibir_mensagme_nome2(nome="Guest"):
       print(f"bem vindo, {nome}")

exibir_mensagme_nome2()