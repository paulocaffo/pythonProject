#  nombre = 'César'
#  apellido = 'Caffo'
#  edad = 30
#  print('Soy ' + nombre + ' ' + apellido + ' y tengo '+str(edad)+' años')
# texto = 'Soy ' + nombre + ' ' + apellido + ' y tengo '+str(edad)+' años'
# print(texto)

# Calculadora de IMC
# IMC = Peso / (Altura x Altura)
# < 19: delgadez
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# >30: obesidad

def calcularIMC(peso,alturaEnMetros):
     imc = round((peso / (alturaEnMetros * alturaEnMetros)), 2)
     return imc

def solicitarIMC():
    peso = float(input('Put your weight in kg '))
    alturaEnCM = int(input('Put you height in cm '))
    alturaEnMetros = alturaEnCM / 100
    #imc = round((peso / (alturaEnMetros * alturaEnMetros)), 2)
    imc = calcularIMC(peso, alturaEnMetros)

    print('Your IMC is ' + str(imc))

    if imc < 20:
        print('Estado de delgadez')
    if 20 <= imc < 26:
        print('Peso normal')
    if 26 <= imc < 30:
        print('Sobrepeso')
    if imc >= 30:
        print('Obesidad')

solicitarIMC()