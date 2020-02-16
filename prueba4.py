from io import open
import pickle


fichero = open("lena.jpg",'rb')

fichero2  = open("lena2.jpg",'wb')

lista = pickle.load(fichero)

print(lista)
