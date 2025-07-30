# Dictionaries in Python
my_dict = dict()
print(type(my_dict))
my_other_dict = {}
print(type(my_other_dict))
my_other_dict = {"Nombre":"Federico","Apellido":"Morales","Edad":45, 1:"Python"}
my_dict = {"Nombre":"Federico",
           "Apellido":"Morales",
           "Edad":45, 
           "Lenguajes":{"Python", "Swift","kotlin"},
           1:1.75
}
print(my_other_dict)
print(my_dict)
print(len(my_other_dict)) # cuatro elementos
print(len(my_dict)) # cinco elementos
print(my_dict["Nombre"]) # Federico
print(my_dict["Apellido"]) # Morales
print(my_dict["Edad"]) # 45
print(my_dict[1]) # 1.75
print(my_dict["Lenguajes"]) # {'Python', 'Swift', 'kotlin'}
#my_dict.pop("Edad") # Elimina el elemento con la clave "Edad"
print(my_dict)
# del my_dict["Edad"] otra forma de eliminar
print("Federico" in my_dict) # False porque "Federico" no es una clave
print("Nombre" in my_dict) # True porque "Nombre" es una clave
print("Python" in my_dict["Lenguajes"]) # True porque "Python" es un elemento del conjunto asociado a la clave "Lenguajes"
print(my_dict.get("Nombre")) # Federico
print(my_dict.get("Edad")) # None porque "Edad" fue borrado antes con pop
print(my_dict.keys()) # Imprime las claves del diccionario
print(my_dict.values()) # Imprime los valores del diccionario
print(my_dict.items()) # Imprime los pares clave-valor del diccionario
print(my_dict.fromkeys(["Python", "Java"], "Lenguajes")) # Crea un nuevo diccionario con claves de la lista y el mismo valor para todas
my_new_dict = my_dict.fromkeys(my_dict) # Creo un diccionario nuevo con las mismas claves
print(my_new_dict) # Imprime el nuevo diccionario con las mismas claves pero sin valores
my_new_dict = my_dict.copy() # Copia el diccionario original
print(my_new_dict) # Imprime el nuevo diccionario copiado
my_new_dict = my_dict.fromkeys(my_dict, [""])
print(my_new_dict) # Imprime el nuevo diccionario con las mismas claves y el mismo valor para todas
print(list(my_new_dict)) # Imprime las claves del diccionario como una lista
print(tuple(my_new_dict)) # Imprime las claves del diccionario como una tupla
print(set(my_new_dict)) # Imprime las claves del diccionario como un conjunto