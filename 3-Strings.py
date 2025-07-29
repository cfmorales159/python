# Strings
my_string = "My String"
my_other_string = 'My Other String'
print(len(my_string))  # Length of the string
print(len(my_other_string))  # Length of the other string    
# ver el espacio luego de \n 
my_new_string = "Este es mi nuevo string \ncon salto de linea"
print(my_new_string)  # Print the new string with a newline character
my_tab_string = "\t \t \tEste es mi string con tabulacion"
print(my_tab_string)  # Print the string with a tab character
# la doble barra evita la tabulación, el salto de línea esta activo
my_scape_string = "\\tEste es mi string con \n\"comillas\""
print(my_scape_string)  # Print the string with escaped quotes
# Formateo de cadenas
name, surname, age = "Federico", "Morales", 45
print("My name is {} and my surname is {} and Im {} years old" .format(name, surname, age))
# En la sigiente linea ya le das el formato directamente a la cadena, se evita que se
# se le pasen otro tipo de datos que no coincidan con el formato
print("My name is %s and my surname is %s and Im %d years old" % (name, surname, age))
# Lee directamente lo ingresado
print(f"My name is {name} and my surname is {surname} and Im {age} years old")
# Desempaquetado de cadenas
language = "python"
a, b, c, d, e, f = language  # Unpacking the string
print(a, b, c, d)  # Print each character of
print(a, b, c, d, e, f)  # Print all characters of the string
# Division de cadenas
language_slice = language[0:3]  
language_slice = language[0:] 
language_slice = language[-3] 
print(language_slice)  # Print the sliced string
# reverso de cadenas
language_reverse = language[::-1]
print(language_reverse)  # Print the reversed string
# Funiones del sistema
print(language.capitalize())  # Convert the string to uppercaseprint(language.capitalize())  
print(language.upper())  
print(language.count("t"))  # Count occurrences of 't' in the string
print(language.upper().isupper())  # Count occurrences of 'T' in the uppercase string
print(language.lower().islower())  # Check if the string is in lowercase
print(language.startswith("Py"))  # Check if the string starts with 'Py'