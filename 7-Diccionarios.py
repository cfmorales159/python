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