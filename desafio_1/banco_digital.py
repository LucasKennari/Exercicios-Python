usuario = "lucas"
saldo = 0
limite_para_saque = 500
numero_de_saques = 0 
LIMITE_SAQUE = 3

extrato = ""

def banco_digtal(extrato, saldo,numero_de_saques):
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

                     elif valor_de_saque > 0:      
                            saldo -= valor_de_saque
                            extrato += msg_saque.format(usuario,"saque".upper(), valor_de_saque, saldo)
                            print(msg_saque_sucesso)
                            numero_de_saques += 1
                     else: 
                            print(erro_msg_valor)

              elif operacao == "d":
                     print(f"{msg_operacao} Deposito")
                     valor_de_deposito = float(input("Digite o valor a ser depositado: \n"))

                     if valor_de_deposito < 0:
                            print(erro_msg_valor)
                            break

                     else:
                            saldo+= valor_de_deposito
                            extrato += msg_deposito.format(usuario.title(), "deposito".upper(), valor_de_deposito,saldo)
                            print(msg_deposito_sucesso)

              elif operacao == "e":

                     print(f"{msg_operacao} Extrato")
                     if extrato == "":
                            print(msg_sem_extrato)
                            print("##### EXTRATO ##### \n")
                            print(f"Saldo Atual: {saldo:.2f}\n")
                            print("###############")
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

Operacao falhou.
Tente novamente...

'''
msg_deposito = """
###### {1} ######
Conta: {0},
Valor depositado: R$ {2:.2f}
Saldo atual: R$ {3:.2f}
#################
"""
msg_saque = """
###### {1} ######
Conta: {0},
Valor sacado: R$ {2:.2f}
Saldo atual: R$ {3:.2f}
#################
"""

msg_operacao_falhou = "Operação falhou:"
msg_saque_sucesso = "Saque efetuado com sucesso! confira seu saldo!"
msg_sem_extrato = "Você possui nenhuma movimentação bancária"
msg_limite_de_qtd_saque = f"{msg_operacao_falhou} Limite para saque extendido !"
msg_limite_de_valor_do_saque = f"{msg_operacao_falhou} O valor de saque está além do limite possível."
msg_saldo_insuficiente = f"{msg_operacao_falhou} Saldo insuficiente!"

banco_digtal(extrato,numero_de_saques,saldo)

