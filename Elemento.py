from zope.interface import implementer
from IElemento import Ielemetos
from Lista import Lista
from Nodo import Nodo
@implementer(Ielemetos)
class Elementos:
    __Coleccion = Lista

    def __init__(self):
        self.__Coleccion = Lista()

    def insertarElemento(self, elemento, pos):
        try:
            self.__Coleccion.insertar(elemento, pos)
        except IndexError:
            raise IndexError
    def agregarElemeto(self, elemento):
        self.__Coleccion.agregar(elemento)
    def MostrarElemento(self, pos):
        try:
            return self.__Coleccion.muestra(pos)
        except IndexError:
            raise IndexError
    def Mostrar(self):
        aux=""
        for element in self.__Coleccion:
            aux += "\n-Modelo: {} \n \t -Puertas: {} \n \t -Precio: {}".format(element.getmodel(), element.getcantp(), element.Importe())
        return aux
    def menorprecio(self):
        return min(self.__Coleccion, key=lambda p: p.getpb())

    def base(self, patente):
        i = 0
        while i < len(self.__Coleccion) and self.__Coleccion.muestra(i).getpatente()!= patente:
            i+=1
        if i < len(self.__Coleccion):
            return self.__Coleccion.muestra(i)
    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__, 
            Elementos=[elemento.toJSON() for elemento in self.__Coleccion]
        )