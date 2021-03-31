import os
import threading
from queue import Queue

def ordenarYEscribir(inicio, final, ruta, listaDeNumeros):
    
    try:
        bloquea.acquire()
        listaOrdenada = listaDeNumeros[inicio:final]
        print(listaOrdenada)
        listaOrdenada = listaOrdenada.sort()
        
        with open("resultadop2.txt", "a") as archivo:
            for num in listaOrdenada:
                archivo.write("{},".format(num))
    except Exception as err:
        print("Algo salio mal Error:  {}".format(err))
    finally:
        bloquea.release()

def calcularTamanioArchivo(ruta=None, numHilos=None):
    tamanioArchivo = os.stat(ruta).st_size
    cantidadALeerEnHilos = tamanioArchivo/numHilos
    lineas = []
    numeroDeNumeros = 0
    print(tamanioArchivo)
    with open(ruta) as archivo:
        lineas = archivo.readlines()
        lineas = lineas[0].split(",")
    numeroDeNumeros = len(lineas)
    lineas = [int(x) for x in lineas]
    return {
        'tamanioarchivo' : tamanioArchivo,
        'totalnumeros' : numeroDeNumeros,
        'cantidadentrehilos' : numeroDeNumeros//3,
        'listanumeros' : lineas
    }

def crearHilos(numeroHilos, seccion, totalnumeros, listaNumero, ruta):
    inicio = 0
    final = seccion
    for num in range(numeroHilos):
        
        hilo = threading.Thread(
                name='Hilo %s'%num,
                target=ordenarYEscribir,
                args=(inicio, final, ruta, listaNumero),
                daemon=True
        )
        inicio = seccion*(num+1)
        if num == numeroHilos-1:
            final += (final+1)
        else:
            final += final
        hilo.start()
    
    hiloPrincipal = threading.main_thread()

    for hilo in threading.enumerate():
        if hilo is hiloPrincipal:
            continue
        hilo.join()

numHilosUsuario = int(input("Numero de hilos: "))

rutaArchivo = "/home/m01/Documents/redesdos/parcialuno/practicasenclase/randompractica2.txt"

data = calcularTamanioArchivo(ruta=rutaArchivo, numHilos=numHilosUsuario)
bloquea = threading.Lock()
crearHilos(numHilosUsuario, data['cantidadentrehilos'],data['totalnumeros'], data['listanumeros'], rutaArchivo)


