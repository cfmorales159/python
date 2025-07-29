# Sets
my_set = set()  # Creating an empty set
print(type(my_set))  # Check the type of my_set
my_other_set = {}
print(type(my_other_set))  # This will show that my_other_set is a dictionary, not a set
my_other_set = {45, 1.75, "Federico", "Morales"}
print(my_other_set)  # Print the set
print(type(my_other_set))  # Check the type of my_other_set
print(len(my_other_set))  # Print the length of the set
my_other_set.add("Nuevo Elemento")  # Adding an element to the set
print(my_other_set)  # Print the set after adding an element, un set no es ordenado
# su forma de guardar es desordenada
# print(my_other_set[0])  # This will raise an error because sets do not support indexing
my_other_set.add("Nuevo Elemento")
print(my_other_set) 
# Se observa que cada vez que se agrega un elemento que ya existe,
# no se agrega de nuevo
# y lo imprime en otro orden
# Un set no admite duplicados
# Para comprobar si un elemeto existe dentro de un set
print("Federico" in my_other_set)  # Check if "Federico" is in the set
print("Otro" in my_other_set)  # Check if "Otro" is in the set
# Para eliminar un elemento de un set
my_other_set.remove("Nuevo Elemento")  # Remove "Nuevo Elemento" from the set
print(my_other_set)  # Print the set after removing an element
my_other_set.clear()  # Clear the set
print(my_other_set)  # Print the set after clearing it
# Para eliminar un set completo
del my_other_set  # Delete the set
#print(my_other_set)   This operation will raise an error because my_other_set was removed
my_other_set = {45, 1.75, "Federico", "Morales"}
my_other_set.pop()
print(my_other_set)  # Print the set after popping an element
# El método pop elimina un elemento aleatorio del set
# y lo devuelve, pero no se puede predecir cuál será el elemento eliminado
# Para crear un set a partir de una lista
my_set = {"Federico", "Morales", 45}
my_list = list(my_set)  # Convert the set to a list
print(type(my_list)) 
print(my_list[0]) # Access the first element of the list
# No se puede confiar en este orden, va cambiando en cada print
# Ahora voy a unir dos sets
my_other_set = {"kotlin","Swift", "Java", "Python"}
my_new_set = my_set.union(my_other_set)  # Combine two sets
print(my_new_set)  # Print the combined set 
# Recordar que los set no admiten duplicados
# es decir en cada union que  haga siempre aparecen los mismos elementos



