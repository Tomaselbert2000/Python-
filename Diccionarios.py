"""
Fecha de inicio: 21 de enero de 2020.
Autor: Tomas Elbert.
Finalidad: ejercicios sencillos acerca de diccionarios.
"""
### Declaramos el primer diccionario y le asignamos datos respetando la estructura "Clave:valor" ###
Diccionario1={"nombre":"Tomas","genero":"masculino","edad":19}
print(Diccionario1)
### Tambien se pueden escribir los diccionarios de la siguiente manera ###
Diccionario2={
    "nombre":"Juan",
    "edad":25,
    "genero":"masculino"}
print(Diccionario2)
### Ambas son validas pero la 2da puede resultar mas ordenada de cara a almacenar muchos datos juntos y luego leerlos ###
### ¿como acceder a los datos de un diccionario? Mediante la funcion print ###
print(Diccionario1["nombre"])
### Importante: al especificar que clave queremos mostrar se debe hacer con corchetes ###
### Usando listas dentro de un diccionario ###
Lista1=("Alejandro","Nilda")
DiccionarioTomas={
    "Nombre":"Tomas",
    "Edad":19,
    "Padres":Lista1}
print(DiccionarioTomas)
### Luego de los dos puntos se pueden especificar variables como valores de la clave en cuestion ###
### Acceder a la lista en el diccionario ###
print(DiccionarioTomas["Padres"][0:2])
### [0:2] indica a Python que debe imprimir en pantalla los valores que se encuentren dentro de "Padres" y que se encuentren dentro de ese rango ###
### Esto es muy util en caso de acceder a listas con muchos valores juntos ###
###¿como añadir mas valores a un diccionario? De la siguiente forma ###
DiccionarioTomas["Ingresos"]="$1000"
### Vemos como se ha añadido la nueva clave al diccionario ###
print(DiccionarioTomas)
### Al escribir de nuevo y cambiar el valor se puede modificar el mismo ###
DiccionarioTomas["Ingresos"]="$2000"
print(DiccionarioTomas)
### Tambien podemos modificar una clave conservando su valor de la siguiente manera ###
DiccionarioTomas["Familiares"]=DiccionarioTomas.pop("Padres")
print(DiccionarioTomas)
### Importante: al especificar la clave que será removida se la escribe entre parentesis, mientras que al escribir la clave que ocupará su lugar si se hace con corchetes ###
### ¿como eliminar una clave junto con su valor? ###
del(DiccionarioTomas["Familiares"])
print(DiccionarioTomas)
### Mostrar claves y valores del diccionario para almacenarlos en variables ###
Claves = DiccionarioTomas.keys()
Valores = DiccionarioTomas.values()
print(Claves)
print(Valores)
