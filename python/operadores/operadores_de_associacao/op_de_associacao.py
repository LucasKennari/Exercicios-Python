# # O que são?
# # Sao operadores utilizados para verificar se um objeto está presente em uma sequencia

curso = "curso de python"
frutas = ["laranja", "uva", "limao"]
saques = [1500, 100]

# Possui a palavra python na sequencia

expressao_1 = "python" in curso
print(f"Python está presente na variavel curso? {expressao_1}")

## Ele verifica se é extamente o mesmo valor, ou seja, não é case sensitive

expressao_2 = "banana" in frutas
print(f"A palavra banana está presente nas frutas? {expressao_2}")

# 200 Não está na sequencia

expressao_3 = 200 not in saques
print(f"o valor 200 NÃO está presente nos saques? {expressao_3}")
