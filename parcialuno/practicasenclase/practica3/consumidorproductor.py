import os
import threading

porProducir, porConsumir = 100000, 100000

bufferAux = []

semaforoProductor = threading.Semaphore(1)
semaforoConsumidor = threading.Semaphore(0)
semaforoBuffer = threading.Semaphore(1)


def consumidor(nombreArchivo, numArchivo):
    #Nos aseguramos de que se cree el archivo por si no esta y no haya problemas
    with open(nombreArchivo, 'a') as archivoCrear:
        print("Creado...")
    lineas = []
    cont = 0
    while cont<porConsumir:
        print("Consumidor")
        semaforoConsumidor.acquire()
        # Lee todas las lienas que ya ha escrito el productor
        semaforoBuffer.acquire()
        with open(nombreArchivo, 'r+') as archivoConsumidor:
            lineas = [x for x in archivoConsumidor.readlines()]
        
        print("Lista consumidor : {}".format(lineas))
        # bufferAux.pop()
        #Escribimos en el archivos del consumidor lo que se consumio
        with open('consumidor{}.txt'.format(numArchivo), 'a') as archivoConsumidor:
            for linea in lineas:
                archivoConsumidor.write(linea+'\n')
        with open(nombreArchivo, 'w') as archivoConsumidor:
            archivoConsumidor.write('')
        semaforoBuffer.release()
        semaforoProductor.release()
        cont+=1

def productor(nombreArchivo, letra):
    a = 0
    cont = 0
    while cont<porProducir:
        print("Productor")
        a+=1
        producto = letra+'-'+str(a)
        semaforoProductor.acquire() #-1 en los procesos del productor
        # Escribimos en el archivo
        semaforoBuffer.acquire()
        with open(nombreArchivo, 'a') as archivoProductor:
            archivoProductor.write(producto)
        print("Lista productor : {}".format(bufferAux))
        # bufferAux.append(a)
        semaforoBuffer.release()
        semaforoConsumidor.release() #+1 en los procesos del consumidor, osea que ya puede consumir
        cont += 1

def crearHilos():
    rutaActual = os.getcwd()
    letrasProductoras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for num in letrasProductoras:
        archivo = "{}.txt".format(('productor'+str(num)))
        hilo1 = threading.Thread(
                name='Hilo %s'%num,
                target=productor,
                args=(archivo, num),
                daemon=True
        )
        
        hilo2= threading.Thread(
                name='Hilo %s'%num,
                target=consumidor,
                args=(archivo, num,),
                daemon=True
        )
        hilo1.start()
        hilo2.start()
    
    hiloPrincipal = threading.main_thread()

    for hilo in threading.enumerate():
        if hilo is hiloPrincipal:
            continue
        hilo.join()


rutaActual = os.getcwd()
print(rutaActual)

crearHilos()