

soma = 0
indice = 1
media = 0
maiorNumero = 0
menorNumero = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


while indice <= 10: 
       valorDeEntrada = int(input(f"escreva o {indice}* numero\n"))
       soma += valorDeEntrada
       if valorDeEntrada > maiorNumero:
              maiorNumero = valorDeEntrada
       if valorDeEntrada < menorNumero:
              menorNumero = valorDeEntrada
       indice +=  + 1
media = soma / 10

print(f"Maior numero é: {maiorNumero}")
print(f"Menor numero é: {menorNumero}")
print(f"A media dos numeros é: {media}")