saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressao_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
expressao_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

expressao_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(expressao_1)
print(expressao_2)
print(expressao_3)