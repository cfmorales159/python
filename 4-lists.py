# Listas
my_list = list()
my_other_list = []
print(len(my_list))
my_list = [45, 32, 53, 64, 25, 45, 1.75]
print(len(my_list))
my_other_list = [45, 1.75, "Federico", "Morales" ]
print(type(my_other_list))
print(type(my_list))
print(my_list[2])  # Accessing the first element
print(my_other_list[0]) # Accessing the first element
print(my_other_list[2])
print(my_other_list[-3])  # Accessing the third element from the end
print(my_other_list[0:])  # Slicing the list from index 0 to the end
print(my_other_list[0:2])  # Slicing the list from index 0 to index 2
print(my_other_list.count("Federico"))  # Count occurrences of "Federico" in the list
print(my_list.count(45))  # Count occurrences of 45 in the list
age, height, name, surname = my_other_list  # Unpacking the list (desempaquetado)
print(height)
print(my_list + my_other_list)  # Concatenating two lists
# Cambie el tipo, antes era una lista, ahora es un string
# Pyrhon es dinamico y no es necesario declarar el tipo de dato
my_list = "Hola Python"
print(my_list)  # This will print the string, not a list
print(type(my_list))  # This will show that my_list is now a string
my_other_list.append("Claudio")  # Adding an element to the end of the list
print(my_other_list)  # Print the list after appending
my_other_list.insert(1, "Nuevo Elemento")  # Inserting an element at index 1
print(my_other_list)  # Print the list after inserting
my_other_list.remove("Nuevo Elemento")  # Removing the element "Nuevo Elemento"
print(my_other_list)  # Print the list after removing
my_other_list.pop(1)  # Removing the element at index 1
print(my_other_list)  # Print the list after popping
del my_other_list[2]  # Deleting the element at index 2
print(my_other_list)  # Print the list after deletion
my_other_list.insert(1, "Morales")  # Re-inserting "Claudio" at index 1
print(my_other_list)  # Print the list after re-inserting
my_list = [45, 32, 53, 64, 25, 45, 1.75]
my_list.sort(-1)  # Sorting the list in ascending order
print(my_list)  # Print the sorted list
