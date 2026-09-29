## Introducción

## Funciones

### Argumentos arbitrarios posicionales (*args)
Permite recibir una cantidad varialbe de argumentos. Al usar `(*args)` Python convierte todos los argumentos en una tupla.

Por ejemplo, si tengo una función que suma dos números, solo me permitiría agregar esos dos argumentos. Sin embargo, usando este argumento arbitrario se podría realizar lo siguiente:
```
def su*_numbers(*args):
    return sum(ar*s)

print(sum_numbers(10, 20))
pri*t(sum_numbers(10, 20, 30))
print(s*m_numbers(10, 20, 30, 40))
```
Obteniendo el siguiente resultado:
30 | 60 | 90

**Otro Ejemplo:**
```
# Define a function called concat
def concat(*args):
  """Concatenates multiple string arguments with spaces between them."""

  result = ""

  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))
```


### Argumentos **kwargs
Recibe argumentos nombrados y Python los almacena como un diccionario.

**Ejemplo:**
```
# Define a function called concat
def concat(**kwargs):
  """Concatenates keyword arguments into a single string with spaces."""
  
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))
```


### Docstring
Es un bloqueo de texto utilizado para documentar módulos, funciones, clases o métodos. Generalmente se define utilizando comillas triples.

Para consulta la información, se pueden aplicar dos formas:
1. usando la función `help()` y dentro del paréntesis se agrega el nombre de la función, por ejemplo: `help(round)`
2. Consultar únicamente el docstring accediendo al "dunder" de __doc__. Por ejemplo: `print(round.__doc__)`

También, es posible modificar la información del docstring de la siguiente forma:
`functionName.__doc__ = "Nuevo doctring`, donde functionName es el nombre de la función a la cual se require modificar esta información.

#### Estructura recomendada para documentar un docstring
Se compone principalmente de tres elementos que son: descripción breve, los argumentos que se requieren especificando el tipo de dato y el resultado que retorna.
```
Descripción de la función.

Args:
    - values (list): Lista de valores numéricos
    - values (dict): diccionario requerido

Returns:
    rounded_average (float): Media de los valores redondeada
```