import pickle

lista = [1,2,3,4,5]

fichero = open("fichero.pckl","wb")

pickle.dump(lista,fichero)

fichero.close()
