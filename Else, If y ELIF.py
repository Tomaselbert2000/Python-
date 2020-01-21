"""
Fecha de inicio: 21 de enero de 2020.
Autor: Tomas Elbert.
Finalidad: ejercicios sencillos acerca de los condicionales "if", "else" y "elif"
"""
### Ejemplo de uso de If ###
### Declaramos una variable cualquiera y le asignamos un valor, en este caso una suma ###
A=2+5
print(A)
### Establecemos la condicion, que si A es exactamente igual a 7, se imprima en pantalla el texto ###
if A==7:
    print("A es igual a 7")
### Escribir "==" es necesario para poder comparar, ya que un solo signo de igualdad se interppreta como operador de asignacion ###
### Ejemplo de uso de Else ###
B=10+10
print(B)
if B==10+15:
    print("B es igual a 25")
else:
    print("No se cumple la condicion")
### En este caso la condicion de If no se cumple y el interprete recurre a Else y lo ejecuta ###
### Es importante aclarar que las condiciones van identadas, es decir, se presiona enter luego de los dos puntos y en la linea siguiente quedan cuatro espacios ###
### Ejemplo de uso de Elif ###
C=25
print(C)
if C==32:
    print("C es igual a 32")
elif C==28:
    print("C es igual a 28")
elif C==25:
    print("C es igual a 25")
else:
    print("No se cumple la condicion")
### En este ultimo caso se puede ver como el elif actua como acumulacion de condiciones para una misma variable ###
