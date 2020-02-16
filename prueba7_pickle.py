from io import open
import pickle

class Persona:

    def __init__(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


nombres = ["Juan", "Pepe", "Ana"]

personas = []

for n in nombres:
    p = Persona(n)
    personas.append(n)

fichero = open("personas.pckl","wb")
pickle.dump(personas,fichero)

fichero.close()
      
