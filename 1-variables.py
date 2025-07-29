#Variables
my_string_variable = "My String Variable"
print(my_string_variable)
my_int_variable = 5
print(my_int_variable)
my_bool_variable = False
print(my_bool_variable)
# Concatenation de variables en print
print(my_string_variable, my_int_variable, my_bool_variable)
print(type(my_string_variable), type(my_int_variable), type(my_bool_variable))
# Funciones del sistema
print(len(my_string_variable))  # Longitud de la cadena
'''
name = input ("Enter your name : ")
age = int(input ("Enter your age : "))
print("Hello", name, "you are", age, "years old.")
'''
# Cambio de tipo de datos
name = 123
age = "Federico"
print(name)
print(age)
# Force type of data
# No es posible dejar fijo el tipo de dato de una variable en Python, pero se puede cambiar su valor a otro tipo.
# Siempre es posible cambiar el tipo de dato de una variable en Python.
address: str = "My address"

print(type(address))  # This will still print <class 'int'> because we changed the type
