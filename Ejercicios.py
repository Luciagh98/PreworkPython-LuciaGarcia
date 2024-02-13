#Ejercicios Introducción a Python: Enunciados

#Ejercicio 1: Conversor de Temperatura
#Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.

grados_celsius = 20
grados_farenheit = ((grados_celsius * 9 / 5) + 32)

print(grados_farenheit)

#Ejercicio 2: Calculadora de Propina
#Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.

total_de_la_cuenta = 200
propina = total_de_la_cuenta * 0.15
total_restuarante = propina + total_de_la_cuenta

print(total_de_la_cuenta)
print(propina)
print(total_restuarante)

#Ejercicio 3: Verificación de Edad
#Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.

edad = int(input("Dime tu edad: "))
if edad >= 18:
  print ("Eres mayor de edad.")
else:
  print("Eres menor de edad.")

#Ejercicio 4: Contador de Vocales
#Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.

def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

print(contar_vocales("LUCIA"))
print(contar_vocales("lucia"))
print(contar_vocales("Garcia"))

#Ejercicio 5: Suma de Números Pares
#Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

contador = 0
numeros = range(0,101)

for numero in numeros:
	if numero % 2 == 0:
		contador = contador + numero
	else:
		pass
		
print(contador)

#Ejercicio 6: Verificación de Palíndromo
#Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

palabra = input("Dime una palabra: ").lower()

if palabra == palabra [::-1]:
	print(f"La palabra {palabra} es una Palíndromo.")
else:
	print(f"La palabra {palabra} no es un Palíndromo.")

#Ejercicio 7: Calculadora Simple
#Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.
	
valor1 = int(input("Dime un valor numérico: "))
valor2 = int(input("Dime otro valor numérico: "))

operacion_arimetica_simple = input("Dime que operación aritmética simple quieres hacer (SUMAR/RESTAR/MULTIPLICAR/DIVIDIR): ").upper()

if operacion_arimetica_simple=="SUMAR":
	suma = valor1 + valor2
	print(suma)
if operacion_arimetica_simple=="RESTAR":
  resta = valor1 - valor2
  print(resta)
if operacion_arimetica_simple=="MULTIPLICAR":
  multiplicar = valor1 * valor2
  print(multiplicar)
if operacion_arimetica_simple== "DIVIDIR":
  dividir = valor1 / valor2
  print(dividir)

#Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
#Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.

peso = int(input("Dime tu peso: "))
estatura = float(input("Dime tu estatura (separando el decimal con un punto (.)): "))

imc = round((peso / (estatura**2)),2)

print(f"Tu peso es {peso}, y la estatura es {estatura}, por tanto tu IMC es {imc}.")

#Ejercicio 9: Conversor de Divisas
#Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.

dolar = int(input("Dime cuántos dólares quieres convertir: "))
euros = dolar * 0.85

print(f"{dolar} dólares son {euros} euros. ")

#Ejercicio 10: Determinar el Día de la Semana
#Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).

def obtener_dia_semana(numero):
    dias_semana = {
        1: 'Lunes',
        2: 'Martes',
        3: 'Miércoles',
        4: 'Jueves',
        5: 'Viernes',
        6: 'Sábado',
        7: 'Domingo'
    }
    if numero in dias_semana:
        return dias_semana[numero]
    else:
        return 'Número de día no válido. Debe estar entre 1 y 7.'

#Ejercicio 11: Calculadora de Edad
#Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.

from datetime import date

def calcular_edad(año_nacimiento):
    año_actual = date.today().year
    edad = año_actual - año_nacimiento
    return edad

año_nacimiento = int(input("Ingresa tu año de nacimiento: "))

calcular_edad(año_nacimiento)

#Ejercicio 12: Calculadora de Área de un Rectángulo
#Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.

longitud = float(input("Ingresa la longitud del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))

if longitud > 0 and ancho > 0:
  area_rectangulo = longitud * ancho
  print(f"El área del rectángulo es: {area_rectangulo} unidades cuadradas.")
else:
  print("La longitud y el ancho deben ser números positivos.")

#Ejercicio 13: Verificación de Número Primo
#Escribe un programa que determine si un número ingresado por el usuario es primo o no.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero_ingresado = int(input("Ingresa un número para verificar si es primo: "))

if es_primo(numero_ingresado):
  print(f"{numero_ingresado} es un número primo.")
else:
  print(f"{numero_ingresado} no es un número primo.")

#Ejercicio 14: Calculadora de Descuento
#Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.

precio_original = float(input("Ingresa el precio original del artículo: "))

if precio_original >= 0:
  descuento = 0.20  # 20% de descuento
  precio_final = precio_original * (1 - descuento)
  print(f"El precio final después del 20% de descuento es: {precio_final:.2f}")
else:
  print("Por favor, ingresa un precio original válido (número no negativo).")

#Ejercicio 15: Conversor de Tiempo
#Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.

minutos_totales = int(input("Ingresa el número de minutos a convertir: "))

if minutos_totales >= 0:
  horas = minutos_totales // 60
  minutos = minutos_totales % 60
  print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos.")
else:
  print("Por favor, ingresa un número de minutos válido (número no negativo).")

#Ejercicio 16: Contador de Números Pares e Impares
#Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.

lista_numeros = list(map(int, input("Ingresa una lista de números separados por espacio: ").split()))

pares = 0
impares = 0

for numero in lista_numeros:
  if numero % 2 == 0:
    pares += 1
  else:
    impares += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")

#Ejercicio 17: Conversor de Millas a Kilómetros
#Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.

millas = float(input("Ingresa la distancia en millas: "))
    
if millas >= 0:
  factor_conversion = 1.60934
  kilometros = millas * factor_conversion
  print(f"{millas} millas equivalen a {kilometros:.2f} kilómetros.")
else:
  print("Por favor, ingresa una distancia válida (número no negativo).")

#Ejercicio 18: Contador de Palabras
#Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

oracion = input("Ingresa una oración: ")

palabras = oracion.split()
cantidad_palabras = len(palabras)

print(f"La oración tiene {cantidad_palabras} {'palabra' if cantidad_palabras == 1 else 'palabras'}.")

#Ejercicio 19: Verificación de Año Bisiesto
#Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.

año = int(input("Ingresa un año: "))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
  print(f"{año} es un año bisiesto.")
else:
  print(f"{año} no es un año bisiesto.")

#Ejercicio 20: Suma de Números en una Lista
#Crea un programa que sume todos los números en una lista ingresada por el usuario.

lista_numeros = list(map(float, input("Ingresa una lista de números separados por espacio: ").split()))

suma_total = sum(lista_numeros)
print(f"La suma total de los números en la lista es: {suma_total}")