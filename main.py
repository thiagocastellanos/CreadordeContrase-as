import random

caracteres = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
longitud = int(input("Introduzca la longitud de su contraseña : "))

contrasena = ""
for i in range(longitud):
    contrasena += random.choice(caracteres)
print(contrasena)

