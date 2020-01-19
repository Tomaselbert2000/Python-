"""
Fecha de inicio: 16 de enero de 2020.
Autor: Tomas Elbert.
Finalidad: ventana básica de inicio de sesión solo con fines visuales.
"""
### Se importa el módulo tkinter para trabajar con él ###
from tkinter import*
### Se crea la ventana principal ###
ventana=Tk()
### Se determina el tamaño que tendrá la ventana ###
ventana.geometry('400x200')
### Se asigna el titulo de la ventana ###
ventana.title("Inicio de sesión")
### "ventana.mainloop" permite a la ventana mantenerse en ejecucion ###
ventana.mainloop
### Se define la primera etiqueta la cual conforma la presentacion ###
Bienvenido=Label(ventana, text="Bienvenido")
### Se especifica que la etiqueta aparezca en pantalla ###
Bienvenido.pack()
### Etiqueta separador ###
Separador1=Label(ventana, text="______________________________________________")
### Se muestra el separador ###
Separador1.pack()
### Etiqueta que indica al usuario que complete su nombre ###
nombre_de_usuario=Label(ventana, text="Ingresar nombre de usuario o email:")
### Se muestra la etiqueta en pantalla ###
nombre_de_usuario.pack()
### Se define una entrada de texto para el nombre ###
campo_de_texto1=Entry(ventana)
### Se muestra el campo de texto en pantalla ###
campo_de_texto1.pack()
### Creacion de un boton para confirmar la entrada de datos ###
boton1=Button(ventana, text="Aceptar", command=campo_de_texto1.get)
### Se muestra el boton en pantalla ###
boton1.pack()
Separador2=Label(ventana, text="______________________________________________")
Separador2.pack()
### Etiqueta que indica al usuario que introduzca su contraseña ###
contraseña=Label(ventana, text="Ingresar contraseña:")
### Se muestra la etiqueta en pantalla ###
contraseña.pack()
### Campo de texto para la contraseña ###
campo_de_texto2= Entry(ventana)
### Se muestra el 2do campo de texto en pantalla ###
campo_de_texto2.pack()
### Se crea otro boton para confirmar la contraseña ###
boton2=Button(ventana, text="Aceptar", command=campo_de_texto2.get)
### Se muestra el boton en pantalla ###
boton2.pack()
