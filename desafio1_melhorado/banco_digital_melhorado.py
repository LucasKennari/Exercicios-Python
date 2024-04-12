menu = '''

Seja bem-vindo(a), {0}

[1] - Extrato
[2] - Saque
[3] - Depositar
[4] - Transferir
[5] - Editar Perfil
[6] - Sair

'''
usuario_001 = {
       ("agencia"): 00,
       ("conta"): 1,
       ("nome"): "lucas", 
       ("saldo"): 0,
       ("extratos"):[]
                }

regras_de_negocio = []

def banco_digital(*, usuario):
              while True:
                     print(menu.format(usuario["nome"]))
                     opcao = int(input("Digite a operacao desejada \n"))

                     if (opcao == 1):
                            print(msg_operacao, "Extrato.")
                            [print(extrato) for extrato in usuario["extratos"]]

                     elif (opcao == 2):
                            print(msg_operacao)

                     elif (opcao == 3):

                            print(msg_operacao, "Deposito.") 
                            valor = float(input("Digite o valor a ser depositado: \n"))
                            operacao_deposito(usuario=usuario,valor=valor)

                     elif (opcao == 4):
                            print(msg_operacao)
                     elif (opcao == 5):
                            print(msg_operacao)
                     elif (opcao == 6):
                            print(msg_operacao)
                            break
                     else:
                            print(msg_operacao_error)
                            break



msg_extrato = """
###### {5} ######
Agencia : {0}
Conta : {1}
Nome : {2}
Valor : {3:.2f}
Saldo atual : {4:.2f}
###############
"""
msg_operacao_sucesso = "Operacao realizada com sucesso!"
msg_operacao_error = "Operacao inválida..."
msg_operacao = "Operacao selecionada:" 
msg_oopcao_error = "Opcao inválida.\n tente novamente..."


def operacao_deposito(*,usuario, valor):
        if valor <= 0:
              return msg_operacao_error
        else:
              usuario["saldo"] += valor
              usuario["extratos"].append(msg_extrato.format(usuario["agencia"], usuario["conta"], usuario["nome"], valor,usuario["saldo"], "DEPOSITO"))
          
        return msg_operacao_sucesso

# def incremento(arr):
#        i = len(arr)

banco_digital(usuario=usuario_001)