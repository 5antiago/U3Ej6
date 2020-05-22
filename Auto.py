
class auto(object):
    __model = str
    __PB = float
    __color = str
    __cantp = int

    def __init__(self, modelo, pb, color, cp):
        self.__model = modelo
        self.__PB = pb
        self.__cantp = cp
        self.__color = color
    def setpb(self, pb):
        self.__PB = pb
    def getmodel(self):
        return self.__model
    def getpb(self):
        return self.__PB
    def getcolor(self):
        return self.__color
    def getcantp(self):
        return self.__cantp
    def __str__(self):
        return "-Modelo: {} \n -Precio Base: {} \n -Color: {} \n -Puertas: {}".format(self.__model, self.__PB, self.__color, self.__cantp)