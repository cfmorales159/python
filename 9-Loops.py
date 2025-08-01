# Loops
# While Loop
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2 # Increment by 2 until my_condition is no longer less than 10
else:
    print("La condición es mayor o igual a 10, se sale del bucle while")
while my_condition < 20:
    my_condition += 1 # Increment by 1 until my_condition is no longer less than 20
    if my_condition == 15:
        print("Se ha alcanzado el valor 15, se detiene el bucle")
        break
    print(my_condition)

# For Loop
my_list = [45, 32, 53, 64, 25, 45, 1.75]
for element in my_list:
    print(element)  # Print each element in the list
my_tuple = (45, 1.75, "Federico", "Morales")
for element in my_tuple:
    print(element)  # Print each element in the tuple
my_other_set = {45, 1.75, "Federico", "Morales"}
for element in my_other_set:
    print(element)  # Print each element in the set
my_dict = {"Nombre":"Federico",
           "Apellido":"Morales",
           "Edad":45, 
           "Lenguajes":{"Python", "Swift","kotlin"},
           1:1.75
}
for element in my_dict:
    print(element)  # Print each key in the dictionary las claves no los valores
for element in my_dict.values():
    print(element)  # Print each value in the dictionary
    if element == "Edad":
        break
    print("Este elemento no es Edad:", element)  # Print if the value is not "Edad"
else:
    print("Se ha recorrido todo el diccionario, se sale del bucle for")