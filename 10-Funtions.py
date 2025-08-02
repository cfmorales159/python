# Functions
def my_function():
    print("This is my function")   
my_function()

def sum_two_values(a, b):
    print(a + b)
sum_two_values(5, 10)
sum_two_values("h", "k") # are two srings, so it will concatenate them
def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value
my_result = sum_two_values_with_return(10, 20)
print(my_result)
my_result = sum_two_values(2,3 )

def print_name(name, surname):
    print(f"{name},{surname}")
print_name("John", "Doe")
print_name(surname="Doe", name="John")  # keyword arguments

def print_name_with_default(name, surname, alias = "without alias"):
    print(f"{name}, {surname}, {alias}")
print_name_with_default("John", "Doe")
print_name_with_default("John", "Doe", "Johnny")  # overriding default value

def print_text(*text): # el asterisc allows for a variable number of arguments
    print(text)
print_text("Hello", "World", "from", "Python")  # variable number of

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
print_upper_texts("Hello", "World", "from", "Python")  # prints each text in uppercase



