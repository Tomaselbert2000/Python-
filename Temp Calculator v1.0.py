"""
Fecha de inicio: 24 de enero de 2020 primera versión funcional.
Actualización 26 de enero: se ha corregido un error de cálculo en el cual se mostraban valores inexactos al trasladar de Fahrenheit a otras medidas.
Actualización 27 de enero: se ha corregido un error en el cual no se podian ingresar valores con decimales para convertir.
Actualizacion 2 de febrero: correción del valor decimal usado para transferir a Kelvin. Se usará 273 en lugar de 273.15
Autor: Tomas Elbert
Finalidad: conversor de unidades de temperatura sencillo mediante teclado numérico.
v1.0.3
"""
while True:
### while True permite que el programa se reinicie de forma correcta una vez que se finalizan las instrucciones    
### Versión del programa
    print("Temp Converter v1.0.3")
### Separador
    print("..............................................................")
### Se muestra una lista con las temperaturas disponibles para calcular
    print("Grados Celsius, seleccione 1 y presione Enter")
    print("Grados Fahrenheit, seleccione 2 y presione Enter")
    print("Grados Kelvin, seleccione 3 y presione Enter")
### Separador
    print("..............................................................")
    print("Tomando en cuenta la lista anterior, completa el siguiente campo")
### Se pide al usuario que elija un número de acuerdo a la temperatura desde donde se inicia el cálculo
    temp_usuario=int(input("Elige la escala de temperatura desde la cual se hará la conversion: "))
### Mediante condicional if se especifica la cadena a imprimir dependiendo del valor que haya elegido el usuario
### Anidado dentro de cada condicional if se encuentra otro if secundario el cual pregunta al usuario a que temperatura desea calcular
    if temp_usuario==1:
        print("Haz elegido grados Celsius")
        if temp_usuario==1:
            print("Muy bien, ahora elijamos a qué escala de temperatura deseas transferirla")
    if temp_usuario==2:
        print("Haz elegido grados Fahrenheit")
        if temp_usuario==2:
            print("Muy bien, ahora elijamos a qué escala de temperatura deseas transferirla")
    if temp_usuario==3:
        print("Haz elegido grados Kelvin")
        if temp_usuario==3:
            print("Muy bien, ahora elijamos a qué escala de temperatura deseas transferirla")
### La siguiente línea se encarga de avisar al usuario mediante un mensaje de error que ha elegido un valor que no se encuentra en la tabla
    if temp_usuario!=1 and temp_usuario!=2 and temp_usuario!=3:
        print("Valor erróneo")
### Separador
    print("..............................................................")
    print("Grados Celsius, seleccione 1 y presione Enter")
    print("Grados Fahrenheit, seleccione 2 y presione Enter")
    print("Grados Kelvin, seleccione 3 y presione Enter")
    print("..............................................................")
    print("Tomando en cuenta la lista anterior, completa el siguiente campo")
### Se pide al usuario que elija una 2da temperatura para realizar el cálculo
    temp_elegida=float(input("Elige a qué escala de temperatura se hará la conversión: "))
    if temp_elegida==1:
        print("Haz elegido grados Celsius")
    if temp_elegida==2:
        print("Haz elegido grados Fahrenheit")
    if temp_elegida==3:
        print("Haz elegido grados Kelvin")
### Igual que antes, si el usuario elige un valor que no se encuentra en la tabla se mostrará un mensaje de error
    if temp_elegida!=1 and temp_elegida!=2 and temp_elegida!=3:
        print("Valor erróneo")
### En este caso, se especifica al programa que si el usuario elige la misma temperatura para ambos valores no puede realizarse ninguna conversión
    if temp_usuario==temp_elegida:
        print("No es posible realizar conversiones dentro de la misma escala")
    print()
    print()
    print("Entonces, se realizará una conversión desde: ")
### Se determina que mensaje mostrar al usuario dependiendo de lo que haya elegido
    if temp_usuario==1 and temp_elegida==2:
        print("Grados Celsius a grados Fahrenheit")
    elif temp_usuario==1 and temp_elegida==3:
        print("Grados Celsius a grados Kelvin")
    elif temp_usuario==2 and temp_elegida==1:
        print("Grados Fahrenheit a grados Celsius")
    elif temp_usuario==2 and temp_elegida==3:
        print("Grados Fahrenheit a grados Kelvin")
    elif temp_usuario==3 and temp_elegida==1:
        print("Grados Kelvin a grados Celsius")
    elif temp_usuario==3 and temp_elegida==2:
        print("Grados Kelvin a grados Fahrenheit")
    print()
    print()
### Se pide al usuario que ingrese mediante el teclado numérico la cantidad que desea calcular
    grados_usuario=float(input("Ingresar cantidad de grados a convertir: "))
### A continuación se establece como el programa debe calcular la temperatura mediante fórmulas
### Para cada tipo de conversión se asigna una variable diferente
    celsius_fahrenheit=(grados_usuario*1.8)+32
    celsius_kelvin=(grados_usuario+273)
    fahrenheit_celsius=((grados_usuario-32)//1.8)
    fahrenheit_kelvin=(grados_usuario+459.67)*5//9
    kelvin_celsius=(grados_usuario-273)
    kelvin_fahrenheit=(grados_usuario-273)*1.8+32
    if temp_usuario==1 and temp_elegida==2:
        print(celsius_fahrenheit,"ºF")
    elif temp_usuario==1 and temp_elegida==3:
        print(celsius_kelvin,"K")
    elif temp_usuario==2 and temp_elegida==1:
        print(fahrenheit_celsius,"ºC")
    elif temp_usuario==2 and temp_elegida==3:
        print(fahrenheit_kelvin)
    elif temp_usuario==3 and temp_elegida==1:
        print(kelvin_celsius,"ºC")
    elif temp_usuario==3 and temp_elegida==2:
        print(kelvin_fahrenheit)
### Se informa al usuario que el programa ya ha calculado los datos y luego se reinicia
    print("Cálculo finalizado")
    print()
    print()
    print("Reiniciando programa...")
### Separador
    print("..............................................................")
