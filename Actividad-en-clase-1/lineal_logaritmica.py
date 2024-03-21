import time

#Algoritmo de ordenamiento Quicksort de complejidad lineal logaritmico 
def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        menores = [x for x in array[1:] if x <= pivot]
        mayores = [x for x in array[1:] if x > pivot]
        return quicksort(menores) + [pivot] + quicksort(mayores)

# Función para medir el tiempo de ejecución
def medir_tiempo(funcion, *args):
    inicio = time.time_ns()
    # Se ejecuta la función 10 veces
    for _ in range(10):  
        funcion(*args)
    fin = time.time_ns()
    # Tiempo promedio en nanosegundos
    tiempo_promedio = (fin - inicio) / 10 

# Tamaños de arrays
tamanos = [10, 100, 1000, 10000, 100000]

for tamano in tamanos:
    # Array invertido para el peor caso
    mi_array = list(range(tamano, 0, -1))   
    tiempo = medir_tiempo(quicksort, mi_array)
    print(f"Tamaño del array: {tamano}, Tiempo promedio de ejecución: {tiempo} nanosegundos")
