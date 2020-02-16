from io import open

fichero = open("fichero2.txt",'r')

#fichero.seek(3)

#fichero.write(unicode("hola\n"))

#texto_leido=fichero.read()
#texto_leido = fichero.readline(10)
#texto_leido = fichero.readlines()
#print(texto_leido)
#print(texto_leido[0])
#print(len(texto_leido))
#print("posicion -> ",fichero.tell())

with open("fichero2.txt",'r') as fichero:
    for linea in fichero:
        print(linea)
