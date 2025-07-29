# tuplas
my_tuple = tuple()
my_other_tuple = ()
my_tuple = (45, 1.75, "Federico", "Morales")
print(my_tuple)
print(my_tuple[0])
print(type(my_tuple))  # Check the type of my_tuple
my_tuple.count("Federico")  # Count occurrences of "Federico" in the tuple
print(my_tuple.count("Federico"))  # Print the count of "Federico"
print(my_tuple.index("Morales"))  # Get the index of "Morales" in the tuple
# my_tuple[0] = 46     # This will raise an error because tuples are immutable
# Tuples are immutable, so we cannot change their elements
my_other_tuple = (1, 2, 3, 4, 5)
print(my_tuple + my_other_tuple)  # Concatenating two tuples
# convierto de tupla a lista
my_list_from_tuple = list(my_tuple)  # Convert tuple to list
my_list_from_tuple[3] = "Nuevo Elemento"  # Modify the list
print(my_list_from_tuple)  # Print the modified list
