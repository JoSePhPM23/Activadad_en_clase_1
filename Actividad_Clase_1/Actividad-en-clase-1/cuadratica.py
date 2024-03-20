import time

#Algoritmo de ordenamiento burbuja de complejidad cuadrática
def ordenamiento_burbuja(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

# Función para medir el tiempo de ejecución
def medir_tiempo(funcion, *args):
    inicio = time.time_ns()
    # Se ejecuta la función 10 veces
    for _ in range(10):   
        funcion(*args)
    fin = time.time_ns()
    #Tiempo promedio en nanosegundos
    tiempo_promedio = (fin - inicio) / 10
    return tiempo_promedio

# Tamaños de arrays
tamanos = [10, 100, 1000, 10000, 100000]

for tamano in tamanos:
    # Array invertido para el peor caso
    mi_array = list(range(tamano, 0, -1))   
    tiempo = medir_tiempo(ordenamiento_burbuja, mi_array)
    print(f"Tamaño del array: {tamano}, Tiempo promedio de ejecución: {tiempo} nanosegundos")

