from zope.interface import implementer, implements
from Nodo import Nodo
from IElemento import Ielemetos

@implementer(Ielemetos)
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
    def agregarElemeto(self, dato):
        nodo = Nodo(dato)
        nodo.setSig(self.__start)
        self.__start = nodo
        self.__actual = nodo
        self.__tope +=1
    def insertarElemento(self, elemento, pos):
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
    def MostrarElemento(self, pos):
        aux = self.__start
        i = 0
        while i<pos and aux != None:
            aux = aux.getSig()
            i +=1
        if aux == None:
            raise IndexError
        else:
            return aux.getDato()
    def Mostrar(self):
        aux = self.__start
        cadena = ""
        while aux!=None:
            cadena += "\n-Modelo: {} \n \t -Puertas: {} \n \t -Precio: {}".format(aux.getDato().getmodel(), aux.getDato().getcantp(),aux.getDato().Importe())
            aux = aux.getSig()
        return cadena 
    def base(self, patente):
        aux = self.__start 
        while aux!=None and aux.getDato().getpatente()!=patente:
            aux = aux.getSig()
        if aux == None:
            return -1
        else:
            return aux.getDato()
    def menorprecio(self):
        Aux=self.__start
        auto = None
        minimo = 999999999
        while Aux != None:
            if minimo > Aux.getDato().getpb():
                minimo = Aux.getDato().getpb()
                auto = Aux.getDato()
                Aux = Aux.getSig()
        return auto
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
    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__, 
            Elementos=[elemento.toJSON() for elemento in self]
        )
    def __iter__(self):
        return self
    def __len__(self):
        return self.__tope
