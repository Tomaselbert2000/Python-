### Se importan dos librerías para crear datos al azar
while True:
    import random
    import string
    print("Password generator v1.0")
    print()
    security_level=int(input("Please select the number of characters you want for the password: "))
    range(int(security_level))
### Se define una variable que almacena la contraseña genenerada
### Range establece la cantidad total de caracteres de la contraseña, pudiendo modificar el nivel de seguridad de la misma
    password=''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(security_level))
    print("Password generated")
    print(password)
    print("Restarting program...")
    print("........................")

