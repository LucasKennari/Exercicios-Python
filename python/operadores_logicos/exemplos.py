saldo = 1000
saque = 250
limite = 200
conta_especial = True

resultado1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
resultado2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)


print(resultado1)
print(resultado2)