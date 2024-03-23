

def calcularFatorial(numeroDeEntrada):
       soma = 1
       if numeroDeEntrada <= 0 or numeroDeEntrada == 1:
              print("Apenas numeros positivos ou maior que 1")
       else:
              while numeroDeEntrada >= 1:
                     soma *= numeroDeEntrada 
                     numeroDeEntrada -= 1
       return soma

numeroDeEntrada = int(input("Digite um numero de entrada \n"))
fatorial = calcularFatorial(numeroDeEntrada)
print(f"O fatorial do numero {numeroDeEntrada} é {fatorial}")