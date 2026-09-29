# Bloqueo de texto que describe lo que hace una función.


# INFORMACIÓN COMPLETA DE LA FUNCIÓN
print(help(round))
print("_______________")

# OBTENER SOLO EL DOCSTRING
# A los atributos con dos guiones bajos, se les llama dunder, en este caso, accedemos al dunder doc
print(round.__doc__)
print("_______________")


# DOCSTRING PARA FUNCIÓN PERSONALIZADA
list_number = [1,2,3,4,5]
def average(values):
    '''
    ____________________________________________________________
    DOCBASTRING de AVERAGE
    Función que calcula el promedio de una lista
    ____________________________________________________________
    '''
    average_value = sum(values) / len(values)
    rounded_average = round(average_value, 2)
    print(f"Promedio de List number es: {rounded_average}")
    return rounded_average

average(list_number)

# Consultando y actualizando docstring
print(f"Consultando la doscting de la función -average-: {average.__doc__}")
average.__doc__ = "Actualizando docstring"
print(f"Consultando la doscting de la función -average-: {average.__doc__}")

# DOCSTRING MULTILÍNEA
def average_2(values):
    '''
    ___________________________________________________________
    Describir la función, luego indicar los argumentos con su tipo de dato, y finalmente lo que retorna

    Args:
        values (list): Lista de valores numéricos
        
    Returns:
        rounded_average (float): Media de los valores, redondeada a dos decimales
    ___________________________________________________________
    '''

print(f"Estructura de una dosctring en general: \n{help(average_2)}")