from Auto import auto
from datetime import date

class AutoUsado(auto):
    __marca = str
    __km = int
    __year = int
    __patente = str

    def __init__(self, modelo, pb, color, cp, marca, km, y, pat):
        super().__init__(modelo, pb, color, cp)
        self.__marca = marca
        self.__km = km
        self.__year = y
        self.__patente =  pat

    def getmarca(self):
        return self.__marca
    def getkm(self):
        return self.__km
    def getyear(self):
        return self.__year
    def getpatente(self):
        return self.__patente
    def Importe(self):
        importe = float
        if self.__km <100000:
            importe = self.getpb()-(date.today().year-self.__year)*0.01*self.getpb()
        else:
            importe = self.getpb()-(date.today().year-self.__year)*0.02*self.getpb()

        return importe
    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            modelo = self.getmodel(),
                            PB = self.getpb(),
                            color = self.getcolor(),
                            cantp = self.getcantp(),
                            marca = self.__marca,
                            km = self.__km,
                            year = self.__year,
                            patente = self.__patente
                            )
                
        )
    def __str__(self):
        return super().__str__() + "\n-Marca: {} \n -Km: {} \n -Año: {} \n -Patente: {} ".format(self.__marca, self.__km, self.__year, self.__patente)
