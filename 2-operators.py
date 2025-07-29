# Operadores aritméticos
print(2 + 3)  # Suma
print(5 - 2)  # Resta
print(2 * 3)  # Multiplicación
print(5 / 2)  # División
print(5 // 2)  # División entera
print(5 % 2)  # Módulo da el resto de la división
print(2 ** 3)  # Exponente
print(2 + 3 * 4)  # Operadores de precedencia
# El signo + concatenará cadenas
print("HellO" + "hOW ARE YOU")  # Concatenación de cadenas
print("Hello " * 5)  # Repetición de cadenas
print("Hello " * (2**3))  # Repetición de cadenas con exponente repite 8 veces
# operadores de comparación
print(3 > 4)  # Mayor que
print(3 < 4)
print(3 >= 4)  # Mayor o igual que
print(3 <= 4)  # Menor o igual que
print(3 == 4)  # Igual que
print(3 != 4)  # Diferente de
print(3 == 3)  # Igual que
# comparando strings
print("Compare Strings")
print("Hello" == "Hello")  # Igual que
print("Hello" != "Hello")  # Diferente de
print("Hello" == "hello")  # Diferente por mayúsculas y minúsculas
print("Hello" == "Hello ")  # Diferente por espacio al final
print("Hola" >= "Bola")  # Diferente por orden alfabético
print("Along" >= "Hello")
print("aaaa" >= "abaa")  # orden alfabético por ASCII
# operadores lógicos, logica boleana
print("Logical Operators")
print(3 > 4 and "Along" >= "Hello")  # AND
print(3 > 4 or "Along" >= "Hello") 
#print(3 > 4 and not "Along" >= "Hello") 
print(3 < 4 and "Along" <= "Hello")
print(3 < 4 or ("Hola" > "Python" and 4==4) ) # damos prioridad a los paréntesis
print(not (3 < 4))  # estoy negando la condición dentro de los paréntesis
# dentro es verdadero, pero al negarlo es falso
