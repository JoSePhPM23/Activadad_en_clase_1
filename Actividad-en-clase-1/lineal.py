import time

#Suma de arrays complejidad lineal
def suma_array(array):
    suma = 0
    for elemento in array:
        suma += elemento
    return suma

# Función para medir el tiempo de ejecución
def medir_tiempo(funcion, *args):
    inicio = time.time_ns()
    #Se ejecuta la función 10 veces
    for _ in range(10):  
        funcion(*args)
    fin = time.time_ns()
    # Tiempo promedio en nanosegundos
    tiempo_promedio = (fin - inicio) / 10  
    return tiempo_promedio

# Tamaños de arrays
tamanos = [10, 100, 1000, 10000, 100000]

for tamano in tamanos:
    mi_array = list(range(tamano))
    tiempo = medir_tiempo(suma_array, mi_array)
    print(f"Tamaño del array: {tamano}, Tiempo promedio de ejecución: {tiempo} nanosegundos")




