import time

#Algoritmo para la sucesión de Fibonacci de complejidad exponencial
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def medir_tiempo(funcion, *args):
    inicio = time.time_ns()
    #Se ejeceuta la función 10 vececs
    for _ in range(10):  
        funcion(*args)
    fin = time.time_ns()
    # Tiempo promedio en nanosegundos
    tiempo_promedio = (fin - inicio) / 10 
    return tiempo_promedio

#Sucesión de Fibonacci para distintos valores de n
valores_n = [10, 15, 20, 25, 30, 35]

for n in valores_n:
    tiempo = medir_tiempo(fibonacci, n)
    print(f"Para n={n}, Tiempo promedio de ejecución: {tiempo} nanosegundos")

