# # A estética

# Identar código é uma forma de manter o código fonte mais legível e manutenível.
# Mas em Python ela exerce um segundo papel, através da indentacao o interpretador
# consegue DETERMINAR onde um bloco de comando inicia e onde ele termina.

# No Javascript utilizamos as CHAVES {} para determinar um escopo do código
# mas no Python, utilizamos apenas identacao

# # Bloco de comando JS
 
# # function sacar(valor) { // inicio do bloco da funcao
                       
# #        if(saldo >= valor){ // inicio do bloco do if
                          
# #        saldo -= valor

# #        }// final do bloco if

# # } // final do bloco da funcao

# # Bloco de comando Python

# def sacar(int(valor)):
       # if saldo >= valor
              # saldo -=  valor

# # UTILIZANDO ESPACOS

# existe uma convencao em python , que define as boas prátticas para escrita
# de código na linguagem. Nesse documento é indicado utilizar
# 4 espacos em branco por nivel de indentacao, ou seja,
# A cada novo BLOCO adicionamos 4 novos espacos em branco

valor = input("Digitte o valor de saque \n")
saldo = 1400

def sacar (self, valor:float) -> None:
       if self.saldo >= valor:
              self.saldo -= valor
              

# # # o caractere para iniciar bloco é o dois pontos  ":"
# OBS: se não colocar a indentacao, o interpretador do python nao conseguira ler o bloco.
              