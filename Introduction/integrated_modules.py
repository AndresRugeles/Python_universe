import os
import string




# --- MODULE OS --- #

# 1. Obtener el directorio de trabajo actual
work_dir = os.getcwd()
print(f"→ Directorio actual:\n {work_dir}\n")

# 2. Cambiar de directorio
change_dir = os.chdir("../../fomestco")

# 3. Obtener el entorno actual
print(f"Entorno actual: {os.environ}\n")


# --- MODULE STRING --- #

# 1. Convertir todo a minúscula
print(f"Convertir todas las letras a minúscula: {string.ascii_lowercase}")

# 2. Retorna todos números del 0 al 9
print(f"Números del 0 al 9: {string.digits}")

# 3. Retorna todos los caracteres especiales
print(f"Caracteres especiales: {string.punctuation}")