import socket
import pickle

def saveImages(data, index):
    routeImage = '/tmp/images/imageno{}.png'.format(index)
    with open(routeImage, 'wb') as image:
        image.write(data)

indexImage = 0

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)


client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client.bind(("192.168.1.255", 37020))

while True:
    data, addr = client.recvfrom(45000)
    print("Imagen recibida")
    saveImages(pickle.loads(data), indexImage)
    indexImage += 1
