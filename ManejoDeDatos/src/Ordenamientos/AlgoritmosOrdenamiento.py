#! /usr/bin/python
__author__ = "mike"
__date__ = "$14/08/2019 05:02:35 PM$"


#Ordenamiento por insercion
def InsertionSort(lista):
    largo=len(lista) #Asigno el largo de la lista a una variable
    if (largo==0 or largo==1): #Si la lista tiene 0 o 1 elemento, entonces esta ordenada, termina el ciclo
        return
    else: 
        for i in range(1,len(lista)): 
            for j in range(0,i): #Por cada elemento que esta antes del elemento que se esta tomando en cuenta,
                if lista[j]>lista[i]: #Si algun elemento anterior resulta mayor que el elemento que se esta tomando en cuenta
                    lista[j], lista[i] = lista[i], lista[j]
    return lista  #Devuelve la lista para que pueda ser usada.

def main():
    lista = [4,7,9,1,2,5]
    print lista
    print InsertionSort(lista)

if __name__ == "__main__":
    main()
