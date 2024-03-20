import time

#Búsqueda secuencial para encontrar un elemento dado
def busqueda_secuencial(array, elemento):
    for item in array:
        if item == elemento:
            return True
    return False

# Función para medir el tiempo de ejecución
def medir_tiempo(funcion, *args):
    inicio = time.time_ns()  
    funcion(*args)  
    fin = time.time_ns()  
    tiempo_total = fin - inicio  
    return tiempo_total


array = list(range(1000000))  

# Busca elemento en el array
buscar = 999999

# Mide el tiempo de la búsqueda secuencial
tiempo_total = medir_tiempo(busqueda_secuencial, array, buscar)

print(f"El tiempo de la búsqueda secuencial es de: {tiempo_total} nanosegundos")

