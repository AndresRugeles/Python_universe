

preparation_times = [19.23, 15.67, 48.57, 23.45, 12.06, 34.56, 45.67]


# Operaciones
print(f"Tiempo de preparación mas largo: {max(preparation_times)}")
print(f"Tiempo de preparación más corto: {min(preparation_times)}")
print(f"Tiempo total preparación: {sum(preparation_times)}")
print(f"Tiempo total preparación redondeado: {round(sum(preparation_times), 1)}")
print(f"Número de elementos de la lista: {len(preparation_times)}")
print(f"Average: {(sum(preparation_times)/len(preparation_times))}")
print(f"Tiempos ordenados: {sorted(preparation_times)}")
print(f"Tiempos ordenados descendete: {sorted(preparation_times, reverse=True)}")
