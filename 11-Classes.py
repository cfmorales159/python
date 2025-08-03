# Classes
# This file contains a class definition for `Person` and demonstrates its usage.
# Se definen en camelCase la primer letra en mayuscula y el resto en minuscula
class MyEmptyPerson:
   pass
print(MyEmptyPerson)  #
print(MyEmptyPerson())  # prints the memory address of the instance

class Person:
    def __init__(self, name, surname): # Constructor method to initialize the object
        self.name = name
        self.surname = surname
my_person = Person("John", "Doe") # Creating an instance of the Person class
print(my_person.name)  # prints the memory address of the instance
print(f"{my_person.name}, {my_person.surname}")  # prints the name and surname of the person
class Person2:
    def __init__(self, name, surname,alias= "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Full name is a single attribute
    def walk (self):
        print(f"{self.full_name} is walking")


my_person2 = Person2("Axel", "Rose")  # Creating an instance of the Person2 class
print(my_person2.full_name)  # prints the full name of the person
my_person2.walk()  # Calls the walk method of the Person2 instance
my_other_person = Person2("Axl", "Rose", "EL chasca")
print(my_other_person.full_name)  # Creating another instance of the Person2 class
my_other_person.walk()  # Calls the walk method of the second Person2 instance
my_other_person.full_name = "Axl Rose el cantor de la orquesta Guns & Roses"  #   
print(my_other_person.full_name)  # prints the updated full name of the person