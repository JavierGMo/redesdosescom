import os
import threading
from queue import Queue
# /home/m01/Documents/pruebaredesdir
def leerContenidoDeArchivos(ruta, cola):
    mapeoPalabras = {
            'casa'   : 0,
            'jardin' : 0,
            'pelota' : 0,
            'juego'  : 0,
            'amor'   : 0,
            'enojo'  : 0
    }

    
    numeroDePalabras = 0
    rutaDir = ruta
    try:
        with open(ruta) as archivo:
            lineas = archivo.readlines()
            if len(lineas) != 0:
                contenidoDeLineas = lineas[0].split(" ")
                numeroDePalabras = len(contenidoDeLineas)

                #print("Letra: {} del : {}".format(linea, threading.current_thread().getName()))
                for linea in contenidoDeLineas:
                    lineaLimpia = linea.strip(',.\n').lower()
                    if lineaLimpia in mapeoPalabras:
                        mapeoPalabras[lineaLimpia] = mapeoPalabras[lineaLimpia]+1
                #cola.put(numeroDePalabras)
    except Exception:
        print("Esto es un directorio\n")
        rutaDir = '{} -> Esto es un directorio'.format(ruta)
    try:
        cola.put({
            'mapapalabras' : mapeoPalabras,
            'numeropalabras' : numeroDePalabras,
            'ruta' : rutaDir
        })
        bloquea.acquire()
        with open("resultado.txt", "a") as archivoEscritura:
            archivoEscritura.write("Archivo con la ruta: {}\n".format(ruta))
            archivoEscritura.write("Total de palabras: {}\n".format(numeroDePalabras))
            archivoEscritura.write("Palabras a buscar:\n")
            for key in mapeoPalabras:
                archivoEscritura.write("Palabra: {} Numero de incidencias: {}\n".format(key, mapeoPalabras[key]))
            archivoEscritura.write("\n\n")
            for key in mapeoPalabras:
                if mapeoPalabras[key] != 0:
                    archivoEscritura.write("Palabra: {} Porcentaje en las palabras: {}%\n".format(key, (numeroDePalabras/mapeoPalabras[key])))
                else:
                    archivoEscritura.write("Palabra: {} Porcentaje en las palabras: {}%\n".format(key, mapeoPalabras[key]))
            archivoEscritura.write("\n\n\n\n")
    finally:
        bloquea.release()




def crearHilos(listaArchivos, ruta, cola):
    for nombre in listaArchivos:
        archivo = "{}/{}".format(ruta, nombre)
        hilo = threading.Thread(
                name='Hilo %s'%nombre,
                target=leerContenidoDeArchivos,
                args=(archivo, cola,),
                daemon=True
        )
        hilo.start()
    
    hiloPrincipal = threading.main_thread()

    for hilo in threading.enumerate():
        if hilo is hiloPrincipal:
            continue
        hilo.join()


ruta = '.'
cola = Queue()
bloquea = threading.Lock()
#ruta actual o ruta
eleccionRuta = int(input("Ruta actual->0\nEscribir ruta->1\n:"))

if eleccionRuta == 1:
    ruta = input("Escribe tu ruta: ")




listaArchivos = os.listdir(ruta)


numArchivos = len(listaArchivos)
print("Lista de archivos")
print(listaArchivos)

crearHilos(listaArchivos, ruta, cola)

print("\n Total de todos los archivos \n")

for algo in range(cola.qsize()):
    print(cola.get())

