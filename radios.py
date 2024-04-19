# Importamos la librería math para utilizar el valor de pi con 6 decimales
import math

# Definimos la función para calcular la circunferencia
def calcular_circunferencia(radio):
    # Utilizamos el valor de pi con 6 decimales
    pi_6_decimales = math.pi * 1000000
    pi_6_decimales = int(pi_6_decimales)
    pi_6_decimales = float(pi_6_decimales) / 1000000
    # Calculamos la circunferencia
    circunferencia = 2 * pi_6_decimales * radio
    return circunferencia

# Llamamos a la función con los radios especificados
circunferencia_3 = calcular_circunferencia(3)
circunferencia_8 = calcular_circunferencia(8)
circunferencia_10 = calcular_circunferencia(10)

# Imprimimos el resultado en español
print("La circunferencia con un radio de 3 es:", circunferencia_3)
print("La circunferencia con un radio de 8 es:", circunferencia_8)
print("La circunferencia con un radio de 10 es:", circunferencia_10)
