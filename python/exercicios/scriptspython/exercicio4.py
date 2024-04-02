
celsius = 0
kelvin = 0
fahrenheit = 0

temperatura = float(input("Digite a temperatura\n"))

print("Qual unidade de medida dessa temperatura?")
opcao = int(input("1 - Celsius; 2 - Kelvin; 3 - Fahrenheit\n"))


if (opcao == 1):
      kelvin = temperatura + 273.15
      print (f"Unidade Celsius para kelvin: {kelvin} K")

      fahrenheit = (temperatura * 9/5) + 32
      print (f"Unidade Celsius para Fahrenheit: {fahrenheit}° F")

elif opcao == 2: 
       celsius = temperatura - 273.15
       print (f"Unidade Kelvin para Celcius: {celsius}° C")
       
       fahrenheit = (temperatura - 273.15) * 9/5 + 32
       print (f"Unidade Kelvin para Fahrenheit: {fahrenheit}° F")

else:
       celsius = (temperatura - 32) * 5/9
       print (f"Unidade Fahrenheit para Celcius: {celsius}° C")

       kelvin  = (temperatura - 32) * 5/9 + 273.15   
       print (f"Unidade Fahrenheit para Kelvin: {kelvin} K")


