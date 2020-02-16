from io import open

#fichero.seek(0)

llegit = raw_input("introduce una palabra ")
print("he leido "+llegit)

contador=0
palabras = []
repe=0

with open("fichero_palabras.txt",'r') as fichero:
    for linea in fichero:
        print(linea)
        print("longitud {}".format(len(linea)))        
        if(linea.strip("\n\r") == llegit):
            print("es igual")
            repe+=1
        else:
            print("es distint")
            
        palabras.append(linea.strip("\n\r"))
        #palabras.append(linea.decode("utf-8"))
        contador=contador+1

#print("contador val: ",contador)
print("contador val: {}".format(contador))
print "la palabra "+format(llegit)+" esta repe "+format(repe)+" veces"
print(palabras)

print(palabras[0].find("h"))
