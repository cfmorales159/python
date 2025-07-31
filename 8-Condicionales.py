# Conditionals
my_condition = False
if my_condition: # es lo mismo que if my_condition == True:
    print(" Se ejecuta la condición if")
print("La ejecución continúa")
my_condition = 12
if my_condition == 11:
    print("Se ejecuta la condición del segundo if")
else:
    print("No se ejecuta la condición del segundo if")
if my_condition > 11:
    print("Se ejecuta la condición del tercer if")
else:
    print("No se ejecuta la condición del tercer if")
if my_condition > 10 and my_condition < 20:
    print("Se ejecuta si es mayor a 10 y menor a 20")
else:
    print("Es menor que 10")
my_string = ""
if not my_string:
    print("La cadena está vacía")
if my_string == "Mi cadena de texto":
    print("Estas cadenas de texto coinciden")