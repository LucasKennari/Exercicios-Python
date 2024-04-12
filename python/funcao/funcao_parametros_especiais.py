# Parametros especiais

# Por padrão, argumentos PODEM ser passados para uma funcao tanto 
# por POSICAO quanto EXPLICITAMENTE pelo nome.
# Para uma melhor legibilidade e desempenho, faz sentido
# restringir a maneira pelo qual argumentos possam ser passados.
# assim, um desenvolvedor precisa apenas olhar paara a definicao
# da funcao para determinar se os itens são passados
# por posicao,
# por posicao e nome ou
# por nome

# def f(pos1, pos2, / , pos_or_kwd, *, kwd1, kwd2):
#        |                    |             |
#        |                    |             |
#        |        Positional or keyword     |
#        |                                  |
#        |                                  |
# Positional only                       Keyword only

# Tudo que ta até a barra " / ", é por posicao

# # POSITIONAL ONLY # #

# Exemplos #

# # # def criar_carros(modelo, ano, placa, / , marca, motor, combustivel ):
# # #        print(modelo, ano, placa, marca, motor, combustivel)

# VÁLIDO #

# ANTES da barra:
# é obrigado a passar sem o parametro nomeado, ou seja, NOME="VALOR"
# Depois da barra é opcional

# # # criar_carros("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# INVÁLIDO #

#Aqui ja foi passado o parametro nomeado, então não é valido, pois nao respeita a regra.

# # # # criar_carros(modelo="Palio", ano=1999, placa="ABC-1234", marca="fiar", motor="1.0", combustivel="Gasolina")


# # KEY WORD ONLY # # // Para o parametro nomeado é utilizado o asteristico a partir do momento em que deseja-se obrigar a esta prática.

# # # def criar_carros(*, modelo, ano, placa, marca, motor, combustivel ):
# # #        print(modelo, ano, placa, marca, motor, combustivel)

# Valido #

# Aqui é passado o parametro nomeado, pois é obrigado.

# # # criar_carros(modelo="Palio", ano=1999, placa="ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina")

# INVALIDO #

# # # criar_carros("Palio", 1999, "ABC-1234", "fiat", motor="1.0", combustivel="Gasolina")


# # HIBRIDO, POSITIONAL KEY E KEYWORD ONLY. # #


def criar_carros(modelo, ano, placa,/, marca,*, motor, combustivel ):
        print(modelo, ano, placa, marca, motor, combustivel)

# # # Os 2 estão certos 

criar_carros("Palio", 1999, "ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina")
# criar_carros("Palio", 1999, "ABC-1234", "fiat", motor="1.0", combustivel="Gasolina")

# * -> Argumentos nomeados
# / -> argumentos por posicao