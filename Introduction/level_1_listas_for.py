#### NIVEL 1: LISTAS Y CICLOS FOR ####

# Ejericio 1 - Contar Tickets abiertos dento de una lista
tickets = ["Cerrado", "Abierto", "Abierto Partes", "Pendiente", "En viaje", "Cancelado", "Abierto"]
print(f"Elementos de la lista: {len(tickets)}")

#---- Solución 1
count_1 = 0
for element in tickets:
    if "Abierto" in element:
        count_1 += 1
        print(f"Ticket abierto encontrado - Count: {count_1}")
    else:
        print(f"No se encontró Ticket en estado abierto")
print(f"TOTAL(1) Tickes en estado abierto: {count_1}")
print("__________________________")
### Usando in busca una coindidencia similar mas no exacta, mientras que en la solución 2 si está buscando una coincidencia exacta

#---- Solución 2
count_2 = 0
for element in tickets:
    if element == "Abierto":
        count_2 += 1
        print(f"Ticket abierto encontrado - Count: {count_2}")
    else:
        print(f"No se encontró Ticket en estado abierto")
print(f"TOTAL(2) Tickes en estado abierto: {count_2}")
print("__________________________")

# Solución 3
count_3 = 0
tickets_2 = [
    {"id": 1001, "estado": "Abierto"},
    {"id": 1002, "estado": "Cerrado"},
    {"id": 1003, "estado": "Abierto"},
    {"id": 1004, "estado": "Pendiente"}
]

for element_2 in tickets_2:
    if element_2["estado"] == "Abierto":
        count_3 += 1
print(f"TOTAL(3) Tickes en estado abierto: {count_3}")