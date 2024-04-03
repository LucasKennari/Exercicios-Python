# Para criar uma estrutura condicional em cadeia, onde possui dois desvios
# podemos uttilizar a palavra reservada ELSE.


# if se a condicao seja verdadeira.
# caso ao contrário (seja falsa)

saldo = 2000.0
saque = float(input("informe o valor do saque \n"))

if saldo >= saque:
       print("Realizando saque")
else:
       print("saldo insuficiente")