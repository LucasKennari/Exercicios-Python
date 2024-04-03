# # Oque é a estrutura de repeticao
# São estruturas utilizadas para repetir um trecho de código um determinado numero de vezes.
# Esse numero pode ser conhecido previamente ou determinado através de uma expressao lógica

# ex:

# a = int(input("informe um numero inteiro:"))
# print(a)

# repita 2 vezes:
#        a += 1
#        print(a)

# # # =========================== # # # 

# for -> palavra reservad utilizada para PERCORRER um objeto iteravel. Faz sentido
# usar for quando sabemos o numero EXATO de vezes que o nosso bloco de código deve ser executado,
# ou quando queremos percorrer um objeto iteravell

texto = input ("informe um texto: \n")
vogais = "AEIOU"


for letra in texto:
       if letra.upper() in vogais:
              print(letra, end="")
              
## end=" " -> forca o numero ficar um do lado do outro.
              
# o for também possui um ELSE: que sera executado no final do laco