

# -- Argumentos
'''
Valores o estructura de datos que se proporciona a la función.
* Posicionales: los argumentos están en orden y separados por comas. Por ejemplo: round(3.141592, 2)
* Palabra clave (keywords): requiere que se defina el valor de cada argumento usando su nombre. Por ejemplo: round(number=3.141592, ndigits=2)
    - En este ejemplo, ndigits=None es el valor predeterminado de la función round, en este caso, es el valor de cero.
'''

age = [2,6,8,10]
def average_age(age):
    len_age = len(age)
    sum_age = sum(age)
    avg = sum_age/len_age
    return avg
print(f"Average: {average_age(age)}")


# --- EXERCISE --- #

# Uso de argumentos Keyworks
product = 'Wireless Mouse'

# Define clean_text function
# En este ejercicio, vas a crear unaclean_text()función que sustituya los espacios por guiones bajos y,
# si lo deseas, convierta el texto a minúsculas.
product = 'Wireless Mouse'

# Define clean_text function
def clean_text(text, lower=True):
    clean_text = text.replace(' ', '_')
    if lower == False:
        return clean_text
    else:
        # Apply lowercase transformation
        return clean_text.lower()

# Test with default behavior
print(clean_text(product, lower=True))


# Genear correo corporativo
full_name = "Andrés Vargas"
def generate_email(full_name):
    name_parts = full_name.split()
    part_1 = name_parts[0]
    part_2 = name_parts[1]
    email = name_parts[0].lower() + '.' + name_parts[1] + '@dn.com'
    email_2 = name_parts[0].lower() + '.' + name_parts[-1] + '@dn.com'
    return email, email_2, part_1, part_2
email, email_2, part_1, part_2 = generate_email(full_name)

print(f"Parte 1: {part_1}")
print(f"Parte 1: {part_2}")
print(f"Email generado: {email}")
print(f"Email generado -opción alterna-: {email_2}")

# Validar si password está correcto
user_password = "Test123456?"
def validate_password(password):
    import string
    # Check if password is at least 8 characters long
    if len(password) >= 8:
        # Check if password contains a special character
        for char in password:
            if char in string.punctuation:
                return True
    return False

# Call the function and store the result
is_valid = validate_password(user_password)
print("Is the password valid? ", is_valid)