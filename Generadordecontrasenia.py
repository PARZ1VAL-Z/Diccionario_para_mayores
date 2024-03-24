import random
c = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

contra = int(input("Ingrese la longitud de la contraseña:"))

password = ""

print("generando contraseña")

for i in range(contra):
    password += random.choice(c)

print("contraseña generada", password)
