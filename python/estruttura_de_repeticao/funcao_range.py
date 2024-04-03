# # range é uma funcao BUILT-IN do python, ela é usada para produzirr uma sequencia
# # de numeros inteiros a partir de um inicio (inclusivo)
# # para um fim(exclusivo).


# #  se usarmos rrange (i, j)
# sera produzido:

# i, i+1, i+2, i+3,...j-1

# ela recebe 3 argumentos: STOP (obrigatorio), start (opcional) e step (opcional)

#range (stop) -> range object
#range(start, stop[, step]) -> range object

lista = list(range(4)) # [0,1,2,3]
print(lista)

# # for numero in range(0, 11):
# #        print(numero, end=" ") // R: 0, 1, 2, 3, 4, 5, 6, 7 ,8 ,9

# # 0 -> inicio
# # 51 -> final 
# # 5 -> step/ seria de quanto em quanto o valor iria pular

# for numero in range(0, 51, 5):
#        print(numero, end=" ") // R: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
       
## end=" " -> forca o numero ficar um do lado do outro.