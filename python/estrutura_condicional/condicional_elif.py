# elif -> Palavra reservada para gerar condicionais em cadeia.

# exemplo

# IF condicional = 1;
#        fazer alguma coisa
# ELIF condicional = 2:
#        fazer outra coisa
# ELIF condicional = 3:
#        fazer alguma outra coisa
# ...
# ...
# ...
# Else: 
#        entao faca isso

# Exemplo #2

opcao  = int(input("informe uma opcao: \n [1] - Sacar \n [2] - Extrato \n [3] - depositar \n"))
saldo = 10.0

if opcao == 1:
       valor = float(input("Informe a quantia para o saque: \n"))
elif opcao == 2:
       print("Exibindo extrato....")   
elif opcao == 3:
       valor =  float(input("digite um valor a ser depositado \n"))
       saldo += valor
       print(f"seu saldo atual :  {saldo}")
else:
       print("Opcao inválida")