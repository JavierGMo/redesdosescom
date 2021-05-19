import sys
import os

def configurarServer():
    #Actualizar e instalar lo necesario
    os.system('apt update')
    os.system('apt install atftpd')
    os.system('mkdir /srv/tftp -p')
    os.system('chown nobody /srv/tftp -R')

    nuevaConfiguracionatftpd = [
        'USE_INETD=false\n',
        '# OPTIONS below are used only with init script\n',
        'OPTIONS="--tftpd-timeout 300 --retry-timeout 5 --mcast-port 1758 --mcast-addr 239.239.239.0-255 --mcast-ttl 1 --maxthread 100 --verbose=5 /srv/tftp"\n'
    ]
    oldLineas = []
    with open('/etc/default/atftpd', 'r') as archivo:
        oldLineas = archivo.readlines()
        print(oldLineas)

    with open('/etc/default/atftpd', 'w') as archivo:
        auxOld = []
        for old in oldLineas:
            auxOld.append(
                '# '+old.replace('#', '')
            )
        oldLineas = auxOld
        nuevaConfiguracionatftpd += oldLineas
        for configuracion in nuevaConfiguracionatftpd:
            archivo.write(configuracion)

    with open('/etc/inetd.conf', 'r') as archivo:
        oldLineas = archivo.readlines()
        print(oldLineas)

    with open('/etc/inetd.conf', 'w') as archivo:
        for old in oldLineas:
            archivo.write("# "+old)
    os.system('reboot')
def iniciarElServicio():
    os.system('/etc/init.d/atftpd start')
    os.system('netstat -nl | grep -E -i "proto|:69"')

accion = int(input('Que quieres hacer:\n1->configurar el TFTP\n2->inicar el servicio TFTP\n:'))
if accion == 1:
    configurarServer()
elif accion == 2:
    iniciarElServicio()
else:
    print('\nLa opcion que escriste no es valida:{}'.format(accion))
