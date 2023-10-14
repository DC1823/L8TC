import timeit
import matplotlib.pyplot as plt

def function(n):
    if n <= 1:
        return
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("Sequence")
            break

# Tamaños de entrada
input_sizes = [1, 10, 100, 1000, 10000, 100000, 1000000]

# Medición de tiempos de ejecución
execution_times = []
for size in input_sizes:
    stmt = f'function({size})'
    setup = 'from __main__ import function'
    time = timeit.timeit(stmt, setup, number=10)  # Número de ejecuciones para mayor precisión
    execution_times.append(time)

# Impresión de los resultados en una tabla
print("Tamaño de Input  | Tiempo de Ejecución")
print("------------------------------------")
for size, time in zip(input_sizes, execution_times):
    print(f"{size:^16} | {time:.6f} segundos")

# Graficar los resultados
plt.plot(input_sizes, execution_times, marker='o')
plt.title('Tamaño de Input vs. Tiempo de Ejecución')
plt.xlabel('Tamaño de Input (n)')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.xscale('log')  # Usar escala logarítmica en el eje x para visualizar mejor
plt.show()
