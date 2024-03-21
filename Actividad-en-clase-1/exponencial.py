import time

# Algoritmo exponencial para calcular la suma de todos los subconjuntos de un array
def suma_subconjuntos(array):
    total = 0
    for i in range(1 << len(array)): 
        subset_sum = 0
        for j in range(len(array)):
            if i & (1 << j):
                subset_sum += array[j]
        total += subset_sum
    return total

# Función para medir el tiempo de ejecución
def medir_tiempo(funcion, *args):
    inicio = time.time_ns()
    # Se ejecuta la función 10 veces
    for _ in range(10):  
        funcion(*args)
    fin = time.time_ns()
    # Tiempo promedio en nanosegundos
    tiempo_promedio = (fin - inicio) / 10 
    return tiempo_promedio

# Tamaños de arrays
tamanos = [10, 100, 1000, 10000]

for tamano in tamanos:
    mi_array = list(range(tamano))
    tiempo = medir_tiempo(suma_subconjuntos, mi_array)
    print(f"Tamaño del array: {tamano}, Tiempo promedio de ejecución: {tiempo} nanosegundos")


