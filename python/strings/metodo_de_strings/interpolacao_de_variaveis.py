# Em python existem 3 formas de interpolar variaveis em strings
# A primeira é usando o sinal %.
# a segunda é utilizando o método format
# e a ultima é utilizando f strings..

# A primeira forma não é atualmente recomendada, e seu uso em python 3 é raro.

nome = "lucas"
idade = 21
profissao = "programador"
linguagem = "python"

# %s -> para tipos strings
# %d -> valores inteiros
# %s -> vaores de ponto flutuante.

# Exemplo #1 ===============================================

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabnallho como %s e estou matriculado no curso de %s."
        % (nome, idade, profissao, linguagem) ) 

# Exemplo #2 ===============================================

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}") 

# Exemplo #3 ===============================================

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}".format(linguagem,profissao,idade,nome)) 
