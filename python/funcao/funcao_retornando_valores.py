# # Retornando valores # #

# Para retornar um valor, utilizamos a palavra reservada return.
# Toda funcao Python retorna None por padrão. Diferente de outras linguagens de programacao.
# Em python uma funcao pode retornar mais de um valor

def calcular_total(numeros):
       return sum(numeros)

def retorna_antecessor_e_sucesssor(numero):
       antecessor = numero - 1
       sucessor = numero + 1

       return antecessor, sucessor


resposta_calculo = calcular_total([10, 20,35])
resposta_antecesosr_e_sucessor = retorna_antecessor_e_sucesssor(10)

print(resposta_calculo)
print(resposta_antecesosr_e_sucessor)