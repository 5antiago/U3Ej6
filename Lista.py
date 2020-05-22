from Nodo import Nodo
from AutoUsado import AutoUsado

class Lista(object):
    __start = None
    __actual = None
    __indice = int
    __tope = int
    def __init__(self):
        self.__start = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    def agregar(self, dato):
        nodo = Nodo(dato)
        nodo.setSig(self.__start)
        self.__start = nodo
        self.__actual = nodo
        self.__tope +=1
    def insertar(self, elemento, pos):
        aux = self.__start
        i = 0
        elemento = Nodo(elemento)
        while i<pos and aux != None:
            aux = aux.getSig()
            i+=1
        if aux == None:
            raise IndexError
        else:
            elemento.setSig(aux.getSig())
            aux.setSig(elemento)
            self.__tope +=1
    def muestra(self, pos):
        aux = self.__start
        i = 0
        while i<pos and aux != None:
            aux = aux.getSig()
            i +=1
        if aux == None:
            raise IndexError
        else:
            return aux.getDato()
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__start
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSig()
            return dato
    def __iter__(self):
        return self
    def __len__(self):
        return self.__tope
