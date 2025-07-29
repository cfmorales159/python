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
