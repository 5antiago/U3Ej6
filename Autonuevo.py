from Auto import auto

class AutoNuevo(auto):
    marca = ""
    __vesion = str

    @classmethod
    def getmarca(cls):
        return cls.marca
    @classmethod
    def setmarca(cls, marca):
        cls.marca = marca

    def __init__(self, modelo, pb, color, cp, version):
        super().__init__(modelo, pb, color, cp)
        self.__vesion = version
    def getversion(self):
        return self.__vesion
    def Importe(self):
        importe = float
        if self.__vesion.lower() == "full":
            importe = self.getpb()+ self.getpb()*0.12
        else:
            importe = self.getpb() + self.getpb()*0.1
        return importe 
    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            modelo = self.getmodel(),
                            PB = self.getpb(),
                            color = self.getcolor(),
                            cantp = self.getcantp(),
                            marca = self.getmarca(), 
                            version = self.__vesion
                            )
            )
    def __str__(self):
        return super().__str__() + "\n -Marca: {} \n -Version: {}".format(self.getmarca(), self.__vesion)