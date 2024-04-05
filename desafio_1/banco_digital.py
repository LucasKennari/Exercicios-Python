usuario = "lucas"
saldo = 0
limite_para_saque = 500
numero_de_saques = 0 
LIMITE_SAQUE = 3

extrato = ""

def banco_digtal(extrato, saldo):
       while True:
              operacao = input(menu).lower()
             
              if operacao == "s":
                     print(f"{msg_operacao} Saque")
                     valor_de_saque = float(input("Digite o valor de saque: \n "))

                     if numero_de_saques >= LIMITE_SAQUE:
                            print(msg_limite_de_qtd_saque)

                     elif valor_de_saque > limite_para_saque:
                            print(msg_limite_de_valor_do_saque)   

                     elif valor_de_saque  > saldo:
                            print(msg_saldo_insuficiente)   

                     # if (numero_de_saques <= LIMITE_SAQUE) and (valor_de_saque <= limite_para_saque) and (valor_de_saque <= saldo):
                     else:      
                            saldo -= valor_de_saque
                            extrato += msg_saque.format(usuario,"saque", valor_de_saque, saldo)
                            print(msg_saque_sucesso)


              elif operacao == "d":
                     print(f"{msg_operacao} deposito")
                     valor = float(input("Digite o valor a ser depositado: \n"))

                     if valor < 0:
                            print(erro_msg_valor)
                            break

                     else:
                            saldo+= valor
                            extrato += msg_deposito.format(usuario, "deposito", valor,saldo)
                            print(msg_deposito_sucesso)

              elif operacao == "e":

                     print(f"{msg_operacao} Extrato")
                     if extrato == "":
                            print(msg_sem_extrato)
                            break
                     else:
                            print(extrato)

              elif operacao == "t":

                     print(f"{msg_operacao} transferencia")
                     print("Transferencia indisponivel no momento . . . ")

              elif operacao == "x":

                     print(f"{msg_operacao} Sair")
                     break

              else:
                     print("Operacao não encontrada.")


menu = f'''
Bem-vindo(a), {usuario.title()}!

[s] - Saque
[d] - Depósito
[e] - Extrato
[t] - Transferencia
[x] - Sair
'''
msg_operacao = "Operacao solicitada:"
msg_deposito_sucesso = "Depositado com sucesso!!"

erro_msg_valor = '''
Só é possivel depositar valores positivos.
tente novamente...
'''
msg_deposito = """
Conta: {0},
Operacao: {1},
valor depositado: R$ {2}
Saldo total: R$ {3}
"""
msg_saque = """
Conta: {0},
Operacao: {1},
valor sacado: R$ {2}
Saldo total: R$ {3}
"""
msg_saque_sucesso = "Saque efetuado com sucesso! confira seu saldo!"
msg_sem_extrato = "Você não possui nenhum extrato bancário."
msg_limite_de_qtd_saque = "Limite para saque extendido !"
msg_limite_de_valor_do_saque = "O valor de saque está além do limite possível."
msg_saldo_insuficiente = "Saldo insuficiente!"

banco_digtal(extrato)

