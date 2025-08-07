# Exceptions Handling in Python
numberOne, numberTwo = 10, 0
numberTwo = "1" # ingreso una cadena en lugar de un número, lo que va a causar un error 

# Try except block to handle exceptions
# Si existe un Try existe un Except
try:
    print(numberOne + numberTwo)
    print("no hay error")
except ValueError as e:
    print("error 1:", e)
except Exception as err:
    print(err)
#except:
#    print("Ha ocurrido un error")
#else:
#    print("La ejecución fue exitosa")
#finally:
#    print("Esto se ejecuta siempre, haya error o no")
#except ValueError:
#    print("Ha ocurrido un error de tipo ValueError")
#except TypeError:
#    print("Ha ocurrido un error de tipo TypeError")

# Captura de la informacion del error
