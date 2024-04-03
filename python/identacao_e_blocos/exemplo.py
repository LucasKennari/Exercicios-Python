


def sacar(valor):
       saldo = 300
       if saldo >= valor:
              print("valor sacado")
       else:
              print("valor insuficiente")
       print(f"Seu saldo atual é de : R${saldo}")


def depositar(valor):
       saldo = 500
       saldo += valor
       print(f"valor {valor} depositatdo")
       print(f"Seu saldo atual é de : R${saldo}")

depositar(400)
sacar(350)      