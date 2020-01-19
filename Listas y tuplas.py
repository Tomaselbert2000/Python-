"""
Fecha de inicio: 18 de enero de 2020.
Autor:Tomas Elbert.
Finalidad: muestra de ejemplos sencillos acerca del uso de las listas y tuplas, ademas de los métodos que puedan aplicarse.
"""
### IMPORTANTE: los lugares que ocupan los elementos en lista y tuplas se cuentan a partir del cero y no del uno ###
### Se crea una lista usando corchetes ###
Lista1=[1,2,3,4,5,6,7,8,9,0]
print(Lista1[3])
### Para crear una tupla se usan parentesis ###
Tupla1=("perro","gato","maceta","arbol","auto")
print(Tupla1[3])
### Ambas se llaman usando corchetes ###
###Ejemplos de métodos usados con listas ###
Lista2=["Alejandro","Nilda","Maxi","Sebastian"]
print(Lista2)
### Método Append para adjuntar ###
Lista2.append("Tomas")
print(Lista2)
### Se puede agregar una lista a otra lista ###
Lista2.append(Lista1)
print(Lista2)
### Método Extend para ampliar ###
Lista3=["Thiago","Agustin","Abril","Lucia"]
print(Lista3)
Lista3.extend("Nahuel")
print(Lista3)
### En este caso se agrega cada letra ingresada dentro de las comillas ###
### Metodo insert para insertar datos en las listas de forma especifica ###
Lista4=["auto","camioneta","colectivo","moto"]
print(Lista4)
### Seleccionamos un item y lo insertamos a la lista definiendo en que lugar se posicionará ###
Lista4.insert(1,"camion")
print(Lista4)
### Metodo pop para eliminar elementos de una lista ###
Lista5=["orquidea","rosa","margarita"]
print(Lista5)
### Procedemos a eliminar un item de la lista especificando su ubicacion ###
Lista5.pop(1)
print(Lista5)
### Si no se especifica un elemento concreto se eliminará el último item que haya en la lista ###
### Metodo Remove para eliminar un elemento, similar a Pop ###
Lista6=["perro","gato","loro","hamster"]
print(Lista6)
Lista6.remove("perro")
print(Lista6)
### Uso de range() y xrange() para crear sucesiones ###
range(7)
### Se crea el dato pero no sucede nada,ya que solo se almacena en la memoria ###
### Se usa la funcion list() para aplicar range() ###
X=list(range(7))
### List() convierte a range en una lista con ese rango de valores ###
print(X)
### Al ejecutar print no se incluye el siete,ya que el valor especificado en range al principio no es abarcado ademas de que se empieza a contar desde cero y no uno ###
### Tambien se puede especificar un valor de inicio, uno de cierre y otro para establecer "saltos" ###
range(0,30,2)
### El 0 indica el inicio de la sucesion, el 30 indica el final, y el 2 refiere a que se haga ese intervalo ###
Y=list(range(0,30,2))
print(Y)
