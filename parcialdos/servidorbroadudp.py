import os
import socket
import pickle
import time
def getImages():
    imagesFinal = []
    rutaImages = '{}/{}'.format(os.getcwd(), 'images')
    imagesInRoute = os.listdir(rutaImages)
    imagesInRoute = [x for x in imagesInRoute if '.png' in x or '.jpg' in x]
    for image in imagesInRoute:
        with open('{}/{}'.format(rutaImages, image), 'rb') as imageRead:
            imagesFinal.append(imageRead.read(1024))
    return imagesFinal
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.settimeout(0.2)
message = b'Mensaje del server'
images = getImages()
indexImages = 0
while True:
    if indexImages==len(images): indexImages = 0
    server.sendto(pickle.dumps(images[indexImages]), ('192.168.1.255', 37020))
    print('Imagen enviada. Numero :{}'.format(indexImages), flush=True)
    time.sleep(1)
    indexImages += 1
