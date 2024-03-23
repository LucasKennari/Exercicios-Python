qntdDePessoas = 3

idadeMasculino = 0 
qtdDeHomens = 0

idadeFeminino = 0
qtdDeMulheres = 0
idadeEntre18e35 = 0 

alturaFeminino = 0
alturaMasculino = 0

contador = 1

while qntdDePessoas >= contador:

       pessoa =  input(f"{contador} - Digite a sexualidade: masculino ou feminino\n")
       if pessoa != "masculino" and pessoa != "feminino" or not pessoa:
              print("Escreva tudo minusculo e verifique se está correto a categoria")
              contador -= 1
       else :       
              altura = int(input("Digite a altura\n"))
              idade = int(input("Digite a idade\n"))
       
              if pessoa == "masculino":
                     idadeMasculino += idade
                     alturaMasculino += altura
                     qtdDeHomens += 1
              if pessoa == "feminino":
                     alturaFeminino += altura
                     idadeFeminino += idade
                     qtdDeMulheres +=1 
              if idade >= 18 and idade <= 35:
                     idadeEntre18e35 += 1

       contador += 1

mediaDasIdadesMasculina = round((idadeMasculino / qtdDeHomens),2) 
mediaDoGrupo = round((( idadeMasculino + idadeFeminino) / qntdDePessoas),2)
mediaAlturaFeminina = round(( alturaFeminino / qtdDeMulheres), 2)
porcentagemDeIdadeEntre18e35 = round(((idadeEntre18e35 / qntdDePessoas) * 100),2)

print(f"A media da idade do grupo coletado é : {mediaDoGrupo}")
print(f"A media da altura das mulheres é : {mediaAlturaFeminina}")
print(f"media da idade entre os homens é: {mediaDasIdadesMasculina}")
print(f"Percentual de pessoas com idades entre 18 e 35 anos é : {porcentagemDeIdadeEntre18e35}%")
