"""
Fecha de inicio: 12 de enero de 2020
Autor: Tomas Elbert
La finalidad del programa es mostrar una ventana informativa sobre Python e información relacionada.
"""
### Se definen variables que luego se utilizan para la generación de texto ###
Enlace_GitHub="https://github.com/python/"
Enlace_IDLEX="http://idlex.sourceforge.net"
Enlace_PyAr="http://www.python.org.ar"
Enlace_Guía_Tkinter="https://guia-tkinter.readthedocs.io/es/develop/index.html"
Enlace_Ejercicios_Sencillos="https://www.discoduroderoer.es/ejercicios-propuestos-y-resueltos-basicos-en-python/"
Enlace_Stackoverflow='https://es.stackoverflow.com/'
### Llamada al módulo Tkinter para crear una interfaz gráfica ###
from tkinter import*
### Se crea la ventana en primera instancia ###
ventana = Tk()
### Se determina el tamaño inicial de la ventana, en este caso 940x560 ###
ventana.geometry('940x560')
### Se especifica un título para la ventana ###
ventana.title('Guía Python')
### Se crea la etiqueta la cual contiene el texto elegido ###
Etiqueta = Label(ventana,text= "Bienvenido a la guia de inicio en Python")
Etiqueta1 = Label(ventana,text="En esta guia se recopilaran enlaces a sitios y documentación con el fin de ayudar al principiante a comenzar en Python")
Etiqueta2 = Label(ventana,text=" Enlace de sitio IDLEX, muy util para la edición y testeo de código "+Enlace_IDLEX)
Etiqueta3 = Label(ventana,text="Enlace de PyAr, info en español acerca de Python "+Enlace_PyAr)
Etiqueta4 = Label(ventana,text="Guía acerca de Tkinter,uno de los módulos más importantes para la creación de interfaces gráficas "+Enlace_Guía_Tkinter)
Etiqueta5 = Label(ventana,text="Blog de ejercicios con sus respectivas soluciones "+Enlace_Ejercicios_Sencillos)
Etiqueta6 = Label(ventana,text="Sección acerca de Python en GitHub "+Enlace_GitHub)
Etiqueta7 = Label(ventana,text="Stackoverflow "+Enlace_Stackoverflow)
### Se especifica a Python que use esa etiqueta con ese texto para la ventana previamente creada ###
Etiqueta.pack()
Etiqueta1.pack()
Etiqueta2.pack()
Etiqueta3.pack()
Etiqueta4.pack()
Etiqueta5.pack()
Etiqueta6.pack()
Etiqueta7.pack()
### "ventana.mainloop" permite que la ventana que hemos creado se mantenga abierta para su uso ###
ventana.mainloop()
