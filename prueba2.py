from io import open
from os.path import isfile

fichero = open("/home/ubuntu/python/fichero.txt",'r')
#posicion_puntero = fichero.tell()
#print("Posicion del puntero {}".format(posicion_puntero))

#fichero.seek(3)
#print(fichero.read())

res = isfile("fichero.txt")
print("res vale ",res)
print("res vale {}".format(res))

if( res == True):
    print("es un fitxer")
else:
    print("no es")


