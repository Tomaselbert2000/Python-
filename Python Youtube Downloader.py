"""
Autor: Tomas Elbert
Fecha de inicio: 21/06/2020
Fecha de terminacion de primera versión beta: 22/07/2020
Fecha de terminacion de primera versión funcional: 10/08/2020
Finalidad del programa: descarga de archivos desde Youtube mediante consola
Version de Python usada: Python 3.6.0, posteriormente Python 3.8

Este programa ha sido diseñado solo como una simple herramienta para descarga de archivos desde Youtube de forma
totalmente personal y para el entretenimiento.
El desarrollador de este programa no percibe ninguna clase de ingreso o beneficio por el uso del mismo, ya sea por su descarga en si o distribucion de copias.
No se cobrará jamas al usuario por el uso de esta herramienta.
Compilado usando librerías de código abierto.

IMPORTANTE: este programa ha presentado fallos durante su desarrollo al usar las librerias Pytube y Moviepy.
En el caso de PyTube, se ha utilizado Pytube3 como sustituto de Pytube, el cual de vez en cuando no reconoce correctamente los títulos de los enlaces procesados.
Por otro lado, Moviepy ha requerido realizar modificaciones puntuales dentro de su instalacion.

Dentro de la carpeta principal de Moviepy se encuentran las carpetas "audio" y "video". A su vez, en ambas se encuentra una llamada "fx" 
que contienen cada una subcarpeta "all", y dentro de ella un archivo llamado "__init__.py"
el cual en ambas debe ser modificado para correr de forma satisfactoria el programa. Se aclara esto ya que el código original incluido dentro de la instalación
de Moviepy realizada con PyPI difiere del que se ha usado para diseñar y testear este programa, pudiendo generar errores a futuro.

A continuacion se adjunta como se debe ver el código fuente:

##################################################################

/moviepy/audio/fx/all/__init__.py

import pkgutil

import moviepy.audio.fx as fx
from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex

__all__ = [name for _, name, _ in pkgutil.iter_modules(
    fx.__path__) if name != "all"]

for name in __all__:
    exec("from ..%s import %s" % (name, name))

##################################################################

/moviepy/video/fx/all/__init__.py

import pkgutil
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize

import moviepy.video.fx as fx

__all__ = [name for _, name, _ in pkgutil.iter_modules(
    fx.__path__) if name != "all"]

for name in __all__:
    exec("from ..%s import %s" % (name, name))

##################################################################

"""

# se importan los modulos necesarios
import logging as lg # se import el módulo logging para almacenar informacion en caso de un fallo al ejecutarse este programa
import os # modulo necesario para el manejo de rutas en el sistema
from pytube import YouTube # modulo necesario para la interaccion con Youtube
from moviepy.editor import VideoFileClip # modulo necesario para procesar video
from moviepy.editor import AudioFileClip # modulo necesario para procesar audio

log=lg.basicConfig(level=lg.ERROR, filename="app_log.txt",filemode='w') # se crea un archivo de texto con el nombre "app_log.txt" para recabar datos
# en caso de que el programa falle, de ejecutarse correctamente este archivo deberia quedar en blanco

while True:

# el bucle while True se encarga de "reiniciar" el programa una vez que se finalizan las instrucciones

###################################################################
    print("Python Youtube Downloader v1.0\n\n")
###################################################################

# Aviso al usuario acerca de las condiciones bajo las cuales debe usar la herramienta

###################################################################
# siempre que sea posible se usarán \n para hacer saltos de linea y ejecutar menos prints

    print("El uso de este programa es absolutamente gratuito.\nEsta herramienta fue pensada para fines personales y/o privados.\nEl desarrollador no se hace responsable del mal uso de esta herramienta en cuanto a infracciones de derechos de autor.\n\n")

###################################################################

    print("Instrucciones:\nBusque el video que ha elegido y copie el enlace desde la barra de direcciones de su navegador.\nA continuacion, se le pedirá que pegue ese enlace.\nPara pegarlo, simplemente use el atajo de teclado Ctrl+V\nEjemplo:","'www.youtube.com/example_video'\n")

###################################################################

# a continuacion se usa un bloque try&except para definir el flujo del programa
# si el usuario ingresa una URL que no puede ser procesada correctamente, se muestra en pantalla un mensaje que informa
# al usuario sobre esto y la consola se reinicia

###################################################################

    try:    
        link= str(input("Introduzca el enlace a continuación: ")) # dentro de esta linea se captura el enlace que el usuario introduce
        link_quotes= ''.join(link) # esta variable inicialmente es un string de dos comillas simples, a las cuales se les agrega dentro el enlace
        youtube= YouTube(link_quotes) # se crea un objeto dentro de la clase Youtube
        print()
        print()
        print("Título del video: ", youtube.title) # usando el metodo title se muestra el titulo del video tal como figura al buscarlo
        print("* Aviso al usuario: debido a cambios recientes en Youtube, puede suceder que al procesar su solicitud el título del video se muestre como 'Youtube' *\n* Sin embargo, esto no afecta a la descarga del archivo ni su contenido. *")
        print("Autor: ", youtube.author) # el metodo author se encarga de mostrar el canal que ha subido el video
        print("Número de vistas: ", youtube.views) # se muestra el numero de vistas que tiene el video hasta el momento que se ejecuta el programa
        print()
        print()
        print("Elija el tipo de archivo que desea descargar a continuacíon:\nSolo audio, seleccione 1 y presione Enter.\nSolo video, seleccione 2 y presione Enter.\nArchivo completo, audio y video, seleccione 3 y presione Enter.\n")
###################################################################

# dentro del siguiente bucle While, se hace que el programa pida al usuario que introduzca un valor numerico para continuar
# en caso de que el valor se corresponda con alguna de las opciones disponibles, el programa continua la ejecucion
# en caso contrario, el bucle While se encarga de avisar al usuario que ha introducido una opcion invalida y le pide que lo intente nuevamente
# volviendo a ejecutarse el codigo al principio del bucle

###################################################################

        while True:
            selection=int(input("Introduzca el valor elegido a continuación: "))
            print()
            print()
            if selection== 1:
                break
            elif selection== 2:
                break
            elif selection== 3:
                break
            else:
                print("El valor que ha elegido es incorrecto, intente nuevamente.")
                print()
###################################################################
# se pide al usuario que le asigne un nombre al archivo para su descarga posterior

        selection_value= int(selection)
        name_of_file=str(input("Por favor especifique un nombre de archivo para proceder con la descarga: "))
        print()
        print("Correcto, el archivo se guardará como: ", name_of_file)
        print()

# se usa el metodo getcwd (Current Working Directory) del módulo os para obtener el directorio actual sobre el cual trabaja el programa
# e informar al usuario donde se guardará su archivo

        print("La descarga se realizará sobre la siguiente ruta: ", os.getcwd())
        print()

###################################################################
# se usa la libreria pathlib para crear las rutas de los archivos que se crearan más adelante
# primero se usa la ruta obtenida antes con os.getcwd, y al str que lo conforma se le agrega el nombre de archivo y su extension
# ya que los archivos se descargan dentro de la misma ubicacion del programa
# luego se usa el metodo resolve para "normalizar" los str y hacerlos funcionlaes en Windows, ya que se acomodan los backslash's

        video_path= str(os.getcwd())+ str("/") + str(name_of_file) + str(".mp4")
        audio_path= str(os.getcwd())+ str("/") + str("audio") + str(".mp4")
        video_path_resolving= os.path.abspath(video_path)
        audio_path_resolving= os.path.abspath(audio_path)

###################################################################

# se define un objeto que recibe el archivo de audio del video elegido usando el método only_audio
# el mismo es necesario para luego poder unirlo al archivo de video y generar el archivo final que recibe el usuario
        audio_source= youtube.streams.filter(only_audio=True)
        audio_file= audio_source[0] # este objeto filtra solo la primera opcion dentro de las respuestas de archivo de audio posibles

###################################################################
# se define una variable para cada calidad de stream que se desea obtener
# en el caso de los file_(resolution), se encargan de capturar el primer o ultimo stream contenido dentro de la variable que les corresponda
# por ejemplo, stream_144p captura todos los streams que cumplan con la condicion de tener esa resolución
# y file_144p obtiene el primer stream de todos ellos, usando el método first
# en el caso de que se use el método last, el funcionamiento es el mismo solo que se captura el último stream
# la funcionalidad concreta de los métodos first y last es poder darle al usuario la elección de cuál archivo elegir
# entre 30 FPS y 60 FPS
# first se usa para los archivos a 30 FPS y last para los que están a 60 FPS

        stream_144p= youtube.streams.filter(res="144p", file_extension='mp4')
        file_144p= stream_144p.first()
        stream_240p= youtube.streams.filter(res="240p", file_extension='mp4')
        file_240p= stream_240p.first()
        stream_360p= youtube.streams.filter(res="360p", file_extension='mp4')
        file_360p= stream_360p.first()
        stream_480p= youtube.streams.filter(res="480p", file_extension='mp4')
        file_480p= stream_480p.first()
        stream_720p= youtube.streams.filter(res="720p", file_extension='mp4')
        file_720p= stream_720p.last()
        stream_1080p= youtube.streams.filter(res="1080p", file_extension='mp4')
        file_1080p= stream_1080p.last()
        stream_2160p= youtube.streams.filter(res="2160p")
        file_2160p= stream_2160p.last()

###################################################################

# en los siguientes bloques "if-elif" se determina cual archivo debe descargar el programa segun la respuesta que el usuario
# haya introducido

###################################################################

# en esta salida se termina de completar el proceso de descarga de archivos solo de audio
# usando un bloque try&except, de modo de poder solventar un posible error durante la descarga del audio

###################################################################
        try:
            if selection==1:
                print("Iniciando descarga de archivo de audio\nDescargando...")
                audio_file.download(filename=name_of_file)
                print("Archivo descargado correctamente")
        except ConnectionError or ConnectionAbortedError or ConnectionRefusedError or ConnectionResetError:
            print("Ha ocurrido un error al realizar la descarga. Intente nuevamente")

        if selection==2:

# el siguiente bucle While cumple la misma funcion que el anterior, ya que pide al usuario que introduzca un valor.
# en caso de corresponderse con alguna de las opciones se procede con la descarga, de otro modo se avisa al usuario del error
# y se pide que elija nuevamente

            while True:

# con los condicionales siguientes se avisa al usuario en caso de que el video que haya seleccionado no contenga alguna resolución en particular
# cuando alguno de los objetos "stream" no retorna ningun valor, es decir, no se obtienen archivos con la resolucion correspondiente, el objeto
# toma el valor de una lista vacia, entonces se usan los condicionales igualados al string '[]'

                print("Elija la calidad de archivo que desea descargar:\n* El tiempo de descarga varía según la velocidad y las condiciones de red actuales*\n..............................................")
                if str(stream_144p)== '[]':
                    print("No se han encontrado archivos con resolución 144p.")
                if str(stream_240p)== '[]':
                    print("No se han encontrado archivos con resolución 240p.")
                if str(stream_360p)== '[]':
                    print("No se han encontrado archivos con resolución 360p.")
                if str(stream_480p)== '[]':
                    print("No se han encontrado archivos con reolución 480p.")
                if str(stream_720p)== '[]':
                    print("No se han encontrado archivos con resolución 720p")
                if str(stream_1080p)== '[]':
                    print("No se han encontrado archivos con resolución 1080p")
                if str(stream_2160p)== '[]':
                    print("No se han encontrado archivos con resolución 2160p")
                print("\nSe prioriza la descarga de archivos a 60 FPS, en caso de no ser posible se realizará la descarga de archivo a 30 FPS.\nPara archivos con resolución 1080p o superior se recomienda descargar mediante Wi-Fi o Banda Ancha debido al gran tamaño de los archivos.\n")
                print("144p, seleccione 1 y presione Enter\n240p, seleccione 2 y presione Enter\n360p, seleccione 3 y presione Enter\n480p, seleccione 4 y presione Enter\n720p, seleccione 5 y presione Enter\n1080p, seleccione 6 y presione Enter\n2160p, seleccione 7 y presione Enter")
                print("\n..............................................")
                quality= int(input("Introduzca el valor elegido a continuación: "))
                if quality==1:
                    break
                    print()
                elif quality==2:
                    break
                    print()
                elif quality==3:
                    break
                    print()
                elif quality==4:
                    break
                    print()
                elif quality==5:
                    break
                    print()
                elif quality==6:
                    break
                    print()
                elif quality==7:
                    break
                else:
                    print("El valor que ha elegido es incorrecto, intente nuevamente.\n")
###################################################################

# se encuentra el siguiente bloque, el cual se encarga de decidir cual archivo descargar
# segun las preferencias del usuario, de modo que, si se produce un error durante la descarga, el usuario sepa que ha sucedido
# y el programa no se reinicie automaticamente

###################################################################

            try:
                if quality ==1:
                    print("Iniciando descarga de archivo de video.\nDescargando...")
                    file_144p.download(filename=name_of_file)
                    print("Archivo descargando correctamente")
                elif quality ==2:
                    print("Iniciando descarga de archivo de video.\nDescargando...")
                    file_240p.download(filename=name_of_file)
                    print("Archivo descargando correctamente")
                elif quality ==3:
                    print("Iniciando descarga de archivo de video.\nDescargando...")
                    file_360p.download(filename=name_of_file)
                    print("Archivo descargando correctamente")
                elif quality ==4:
                    print("Iniciando descarga de archivo de video.\nDescargando...")
                    file_480p.download(filename=name_of_file)
                    print("Archivo descargando correctamente")
                elif quality ==5:
                    print("Iniciando descarga de archivo de video.\nDescargando...")
                    file_720p.download(filename=name_of_file)
                    print("Archivo descargado correctamente")
                elif quality==6:
                    print("Iniciando descarga de archivo de video.\nDescargando...")
                    file_1080p.download(filename=name_of_file)
                    print("Archivo descargado correctamente")
                elif quality==7:
                    print("Iniciando descarga de archivo de video.\nDescargando...")
                    file_2160p.download(filename=name_of_file)
                    print("Archivo descargado correctamente")
###################################################################

# esta seccion except se encarga de capturar un posible error de conexion durante la descarga e informa al usuario

            except ConnectionError or ConnectionAbortedError or ConnectionRefusedError or ConnectionResetError:
                print("Ha ocurrido un error al realizar la descarga. Intente nuevamente")

###################################################################

# a continuacion se aplican las mismas definiciones que se han aplicado en el bloque anterior
# en este caso se busca mostrar una salida de texto en la consola con las mismas instrucciones para el usuario
# y mientras tanto el programa se encargará de procesar la solicitud de descarga de archivos y unirá los datos de audio y video en un solo archivo


        elif selection==3:
            while True:
                print("Elija la calidad de archivo que desea descargar:\n* El tiempo de descarga varía según la velocidad y las condiciones de red actuales*\n..............................................")
                if str(stream_144p)== '[]':
                    print("No se han encontrado archivos con resolución 144p.")
                if str(stream_240p)== '[]':
                    print("No se han encontrado archivos con resolución 240p.")
                if str(stream_360p)== '[]':
                    print("No se han encontrado archivos con resolución 360p.")
                if str(stream_480p)== '[]':
                    print("No se han encontrado archivos con reolución 480p.")
                if str(stream_720p)== '[]':
                    print("No se han encontrado archivos con resolución 720p")
                if str(stream_1080p)== '[]':
                    print("No se han encontrado archivos con resolución 1080p")
                if str(stream_2160p)== '[]':
                    print("No se han encontrado archivos con resolución 2160p")
                print()
                print("Se prioriza la descarga de archivos a 60 FPS, en caso de no ser posible se realizará la descarga de archivo a 30 FPS.\nPara archivos con resolución 1080p o superior se recomienda descargar mediante Wi-Fi o Banda Ancha debido al gran tamaño de los archivos.")
                print()
                print("144p, seleccione 1 y presione Enter\n240p, seleccione 2 y presione Enter\n360p, seleccione 3 y presione Enter\n480p, seleccione 4 y presione Enter\n720p, seleccione 5 y presione Enter\n1080p, seleccione 6 y presione Enter\n2160p, seleccione 7 y presione Enter")
                print()
                print("..............................................")
                quality= int(input("Introduzca el valor elegido a continuación: "))
                if quality==1:
                    break
                    print()
                elif quality==2:
                    break
                    print()
                elif quality==3:
                    break
                    print()
                elif quality==4:
                    break
                    print()
                elif quality==5:
                    break
                    print()
                elif quality==6:
                    break
                    print()
                elif quality==7:
                    break
                else:
                    print("El valor que ha elegido es incorrecto, intente nuevamente.\n")
# el inicio del bloque try se debe ubicar a tres identaciones desde el comienzo de la linea
# dentro de este bloque try & except se define qué archivo descargará segun la elección del usuario usando condicionales if-elif
# e intentara capturar un error si es que ocurre e informarlo en pantalla

###################################################################

# dentro de cada bloque if-elif se usa el modulo moviepy para compilar el audio y el video dentro de un solo archivo

            try:
                if quality==1:
                    print("Iniciando descarga de archivos\nDescargando video...")
                    file_144p.download(filename=name_of_file)
                    print("Video descargado\nDescargando audio...")
                    audio_file.download(filename="audio")
                    print("Audio descargado")
                    print("\nIniciando compilación de archivos, espere por favor.\n* El tiempo de procesamiento varía según la potencia de su equipo *\n")
                    video_clip= VideoFileClip(video_path_resolving) # se define un objeto con el cual se accede al archivo de video descargado antes, usando como argumento el str de la ruta del archivo
                    audio_clip= AudioFileClip(audio_path_resolving) # se define un objeto con el cual se accede al archivo de audio complementario
                    compilation= video_clip.set_audio(audio_clip) # con el metodo set_audio se superpone el audio al video, el cual no contiene sonido. Ambos duran lo mismo.
                    compilation.write_videofile(filename=str(name_of_file+" nuevo" +".mp4"), fps=30) # se guarda el archivo nuevo en el disco, especificando el nombre que el usuario ha elegido, y aclarando su extension
                    os.remove(str(name_of_file+".mp4")) # se elimina el archivo de video antiguo cuando se finaliza la operacion
                    os.remove("audio.mp4") # se elimina el archivo de audio usado cuando se finaliza la operación
                    print("Archivo compilado correctamente")
                elif quality==2:
                    print("Iniciando descarga de archivos\nDescargando video...")
                    file_240p.download(filename=name_of_file)
                    print("Video descargado\nDescargando audio...")
                    audio_file.download(filename="audio")
                    print("Audio descargado")
                    print("\nIniciando compilación de archivos, espere por favor.\n* El tiempo de procesamiento varía según la potencia de su equipo *\n")
                    video_clip= VideoFileClip(video_path_resolving) # se define un objeto con el cual se accede al archivo de video descargado antes, usando como argumento el str de la ruta del archivo
                    audio_clip= AudioFileClip(audio_path_resolving) # se define un objeto con el cual se accede al archivo de audio complementario
                    compilation= video_clip.set_audio(audio_clip) # con el metodo set_audio se superpone el audio al video, el cual no contiene sonido. Ambos duran lo mismo.
                    compilation.write_videofile(filename=str(name_of_file+" nuevo" +".mp4"), fps=30) # se guarda el archivo nuevo en el disco, especificando el nombre que el usuario ha elegido, y aclarando su extension
                    os.remove(str(name_of_file+".mp4")) # se elimina el archivo de video antiguo cuando se finaliza la operacion
                    os.remove("audio.mp4") # se elimina el archivo de audio usado cuando se finaliza la operación
                    print("Archivo compilado correctamente")
                elif quality==3:
                    print("Iniciando descarga de archivos\nDescargando video...")
                    file_360p.download(filename=name_of_file)
                    print("Video descargado\nDescargando audio...")
                    audio_file.download(filename="audio")
                    print("Audio descargado")
                    print("\nIniciando compilación de archivos, espere por favor.\n* El tiempo de procesamiento varía según la potencia de su equipo *\n")
                    video_clip= VideoFileClip(video_path_resolving) # se define un objeto con el cual se accede al archivo de video descargado antes, usando como argumento el str de la ruta del archivo
                    audio_clip= AudioFileClip(audio_path_resolving) # se define un objeto con el cual se accede al archivo de audio complementario
                    compilation= video_clip.set_audio(audio_clip) # con el metodo set_audio se superpone el audio al video, el cual no contiene sonido. Ambos duran lo mismo.
                    compilation.write_videofile(filename=str(name_of_file+" nuevo" +".mp4"), fps=30) # se guarda el archivo nuevo en el disco, especificando el nombre que el usuario ha elegido, y aclarando su extension
                    os.remove(str(name_of_file+".mp4")) # se elimina el archivo de video antiguo cuando se finaliza la operacion
                    os.remove("audio.mp4") # se elimina el archivo de audio usado cuando se finaliza la operación
                    print("Archivo compilado correctamente")
                elif quality==4:
                    print("Iniciando descarga de archivos\nDescargando video...")
                    file_480p.download(filename=name_of_file)
                    audio_file.download(filename="audio")
                    print("Audio descargado")
                    print("\nIniciando compilación de archivos, espere por favor.\n* El tiempo de procesamiento varía según la potencia de su equipo *\n")
                    video_clip= VideoFileClip(video_path_resolving) # se define un objeto con el cual se accede al archivo de video descargado antes, usando como argumento el str de la ruta del archivo
                    audio_clip= AudioFileClip(audio_path_resolving) # se define un objeto con el cual se accede al archivo de audio complementario
                    compilation= video_clip.set_audio(audio_clip) # con el metodo set_audio se superpone el audio al video, el cual no contiene sonido. Ambos duran lo mismo.
                    os.remove(str(name_of_file+".mp4")) # se elimina el archivo de video antiguo cuando se finaliza la operacion
                    os.remove("audio.mp4") # se elimina el archivo de audio usado cuando se finaliza la operación
                    print("Archivo compilado correctamente")
                elif quality==5:
                    print("Iniciando descarga de archivos\nDescargando video...")
                    file_720p.download(filename=name_of_file)
                    print("Video descargado\nDescargando audio...")
                    audio_file.download(filename="audio")
                    print("Audio descargado")
                    print("\nIniciando compilación de archivos, espere por favor.\n* El tiempo de procesamiento varía según la potencia de su equipo *\n")
                    video_clip= VideoFileClip(video_path_resolving) # se define un objeto con el cual se accede al archivo de video descargado antes, usando como argumento el str de la ruta del archivo
                    audio_clip= AudioFileClip(audio_path_resolving) # se define un objeto con el cual se accede al archivo de audio complementario
                    compilation= video_clip.set_audio(audio_clip) # con el metodo set_audio se superpone el audio al video, el cual no contiene sonido. Ambos duran lo mismo.
                    compilation.write_videofile(filename=str(name_of_file+" nuevo" +".mp4"), fps=30) # se guarda el archivo nuevo en el disco, especificando el nombre que el usuario ha elegido, y aclarando su extension
                    os.remove(str(name_of_file+".mp4")) # se elimina el archivo de video antiguo cuando se finaliza la operacion
                    os.remove("audio.mp4") # se elimina el archivo de audio usado cuando se finaliza la operación
                    print("Archivo compilado correctamente")
                elif quality==6:
                    print("Iniciando descarga de archivos\nDescargando video...")
                    file_1080p.download(filename=name_of_file)
                    print("Video descargado\nDescargando audio...")
                    audio_file.download(filename="audio")
                    print("Audio descargado")
                    print("\nIniciando compilación de archivos, espere por favor.\n\n* El tiempo de procesamiento varía según la potencia de su equipo *\n")
                    video_clip= VideoFileClip(video_path_resolving) # se define un objeto con el cual se accede al archivo de video descargado antes, usando como argumento el str de la ruta del archivo
                    audio_clip= AudioFileClip(audio_path_resolving) # se define un objeto con el cual se accede al archivo de audio complementario
                    compilation= video_clip.set_audio(audio_clip) # con el metodo set_audio se superpone el audio al video, el cual no contiene sonido. Ambos duran lo mismo.
                    compilation.write_videofile(filename=str(name_of_file+" nuevo" +".mp4"), fps=30) # se guarda el archivo nuevo en el disco, especificando el nombre que el usuario ha elegido, y aclarando su extension
                    os.remove(str(name_of_file+".mp4")) # se elimina el archivo de video antiguo cuando se finaliza la operacion
                    os.remove("audio.mp4") # se elimina el archivo de audio usado cuando se finaliza la operación
                    print("Archivo compilado correctamente")
                elif quality==7:
                    print("Iniciando descarga de archivos\nDescargando video...")
                    file_2160p.download(filename=name_of_file)
                    print("Video descargado\nDescargando audio...")
                    audio_file.download(filename="audio")
                    print("Audio descargado")
                    print("\nIniciando compilación de archivos, espere por favor.\n\n* El tiempo de procesamiento varía según la potencia de su equipo *\n")
                    video_clip= VideoFileClip(video_path_resolving) # se define un objeto con el cual se accede al archivo de video descargado antes, usando como argumento el str de la ruta del archivo
                    audio_clip= AudioFileClip(audio_path_resolving) # se define un objeto con el cual se accede al archivo de audio complementario
                    compilation= video_clip.set_audio(audio_clip) # con el metodo set_audio se superpone el audio al video, el cual no contiene sonido. Ambos duran lo mismo.
                    compilation.write_videofile(filename=str(name_of_file+" nuevo" +".mp4"), fps=30) # se guarda el archivo nuevo en el disco, especificando el nombre que el usuario ha elegido, y aclarando su extension
                    os.remove(str(name_of_file+".mp4")) # se elimina el archivo de video antiguo cuando se finaliza la operacion
                    os.remove("audio.mp4") # se elimina el archivo de audio usado cuando se finaliza la operación
                    print("Archivo compilado correctamente")

            except ConnectionError or ConnectionAbortedError or ConnectionRefusedError or ConnectionResetError:
                print("Ha ocurrido un error al realizar la descarga. Intente nuevamente")


###################################################################

# esta seccion except se encarga de capturar el error en caso de que el enlace especificado no funcione
# y avisa al usuario del mismo

    except Exception:
        print("Error.\nEl enlace ingresado no es válido, inténtelo nuevamente.")

###################################################################
    finally:
        print()
        print()
        print("Reiniciando programa...\n###################################################################\n###################################################################")