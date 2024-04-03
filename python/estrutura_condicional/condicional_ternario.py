saldo = 50
saque = 40
status = "sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque!")