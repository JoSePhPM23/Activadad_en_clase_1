import time

#Algortimo de búsqueda binaria complijidad logaritmica
def busqueda_binaria(array, elemento):
    inicio = 0
    fin = len(array) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if array[medio] == elemento:
            return True
        elif array[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1
    return False

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
    #Busca el elemento que no esta en la array
    elemento_a_buscar = tamano + 1  
    tiempo = medir_tiempo(busqueda_binaria, mi_array, elemento_a_buscar)
    print(f"Tamaño del array: {tamano}, Tiempo promedio de ejecución: {tiempo} nanosegundos")
