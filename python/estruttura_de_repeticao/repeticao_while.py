# # Comando while

# É utilizado para repetir um bloco de código várias vezes. Faz sentido usar o while quanmdo não sabemos
# o numero EXATO de vezes que nosso bloco de código deve ser executado


# Exemplo #1 // 

opcao = -1

while opcao != 0:
       opcao = int(input("[1] - Sacar \n[2] - Extrato \n[0] - sair \n"))
       
       if opcao == 1:
              print("sacando..")
       elif opcao == 2:
              print("exibindo o extrato ...")

# Exemplo #2 //

while True:
       numero = int(input("Informe um numero:"))

       if numero == 10:
              break

       print(numero)

#Exemplo #3 // Vai pular todos os numeros pares e só mostrar impares.

for numero in range(100):

       if numero % 2 == 0:
              continue

       print(numero, end=" ")